from flask import Flask, render_template, request, redirect, url_for, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin, LoginManager, login_required, logout_user, current_user, login_user

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)
admin = Admin(app, name='Admin', template_mode='bootstrap3')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    accountType = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(120), nullable=False, unique=True)
    
    password_hash = db.Column(db.String(128), nullable=False)

    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True
    def get_id(self):
        # return self.username
        return self.id
    def is_authenticated(self):
        return self.authenticated
    def is_anonymous(self):
        return False

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(50), nullable=False)
    professor = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    student = db.Column(db.String(50), nullable=False)
    studentGrade = db.Column(db.Integer, nullable=False)

    def __init__(self, cName, pName, time, cap, stu, stuGrade):
        self.courseName = cName
        self.professor = pName
        self.time = time
        self.capacity = cap
        self.student = stu
        self.studentGrade = stuGrade

    

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Course, db.session))


# Login Page for Student
@app.route("/", methods=['GET', 'POST'])
def index():
    name = None
    password = None
    form = LoginForm()
    # Validate From
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password_hash:
                login_user(user)

                flash("Login Succesfull")
                if user.accountType == 'student':
                    return redirect(url_for('StudentDash'))
                else:
                    return redirect(url_for('ProfessorDash'))
            else:
                flash("Wrong Password - Try again!")
                return render_template('LoginPage.html',
                               username='',
                               password='',
                               form=form)
        else:
            flash("User does not exist.")
            return render_template('LoginPage.html',
                               username='',
                               password='',
                               form=form)
        # name = form.name.data
        # password = form.password.data
        # form.name.data = ''
        # form.password.data = ''
        flash("Form Submitted Successfully")
    else:
        return render_template('LoginPage.html',
                               username='',
                               password='',
                               form=form)
        # return redirect(url_for('StudentDash'))


@app.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))
    # return render_template('/')

@app.route("/addRemove/", defaults={'CourseName':None})
@app.route("/addRemove/<CourseName>")
@login_required
def addRemoveCourse(CourseName='RandomClass'):
    print("Name of course")
    print(CourseName)
    curUser = current_user
    # user = User.query.filter_by(username=form.username.data).first()
    db.session.query(Course).filter_by(courseName=CourseName, student=curUser.name).delete();
    db.session.commit()

    return redirect(url_for('StudentDash', ownCourse=False))

@app.route("/addStudentToCourse/<CourseName>")
@login_required
def addStudent(CourseName):

    courses = Course.query.order_by(Course.courseName)
    totalStudentCounts = getTotalStudentCount(courses)

    specificCourse = getSpecificCourse(courses, CourseName)
    specificCourseCapacity = specificCourse.capacity
    print("inside add student function")
    print(totalStudentCounts)
    print("selected course capacity")
    print(specificCourseCapacity)
    if totalStudentCounts[CourseName] >= specificCourseCapacity:
        return redirect(url_for('StudentDash', ownCourse=False))
    else:
        newStudentToCourse = Course(CourseName, specificCourse.professor, specificCourse.time, specificCourseCapacity, current_user.name, 100)
        db.session.add(newStudentToCourse)
        db.session.commit()
        return redirect(url_for('StudentDash', ownCourse=False))

    

    print("end of add student function")

def getSpecificCourse(courseList, courseName):
    for course in courseList:
        if course.courseName == courseName:
            return course

def courseAtMaximumCapacity(courseName):
    if courseName == None:
        return False
    
    

@app.route("/switchStuDash/")
@login_required
def switchStuDash():
    return redirect(url_for('StudentDash', ownCourse=False))

# Dashboard Page for Student
@app.route("/StudentDashboard/", defaults={'ownCourse':None}, methods=['POST', 'GET'])
@app.route("/StudentDashboard/<ownCourse>", methods=['POST', 'GET'])
@login_required
def StudentDash(ownCourse):
    # ownCourse = ownCourse.lower() == 'true'
    if ownCourse == None:
        ownCourse = True
    else:
        ownCourse = False
    user = current_user
    # # print(user)
    userFullName = user.name
    print(userFullName)
    # grab all the courses in the database
    courses = Course.query.order_by(Course.courseName)
    # Grab all the courses from the database that student is in
    personalCourses = Course.query.filter_by(student=userFullName)
    # count how many i get by the query above

    inputCourse = personalCourses
    allCourse = courses
    count = inputCourse.count()
    # print(count)

    # dictionary of all students with their count per class
    totalStudentCounts = getTotalStudentCount(courses)
    # dictionary of count for the classes the user is in
    studentCountOfPersonalSchedule = getStudentsEnrolledDictionary(personalCourses, courses)

    # an array of all the classes (even if the student isn't in it, and there are no duplicates)
    uniqueAllClassList = getUniqueInputList(courses)
    
    # print(f"ownCourse {ownCourse}")
    # getStudentsEnrolledDictionary(personalCourses, courses)


    # print("kk")
    # return render_template("StudentDashboard.html", fullName="jess")
    return render_template("StudentDashboard.html", 
                           fullName=current_user.name,
                           courses = inputCourse,
                           allCourses=allCourse,
                           courseCount = count,
                           studentCountOfPersonalSchedule = studentCountOfPersonalSchedule,
                           ownCourse=ownCourse,
                           totalStudentCounts=totalStudentCounts,
                           uniqueAllClassList=uniqueAllClassList)

def getUniqueInputList(inputList):
    listSet = set()
    listArr = []
    for item in inputList:
        if item.courseName not in listSet:
            listSet.add(item.courseName)
            listArr.append(item)
    return listArr

def getTotalStudentCount(inputList):
    if inputList == None:
        return {}
    studentCount = {}
    print(inputList.count())
    for i in inputList:
        if i.courseName not in studentCount:
            studentCount[i.courseName] = 1
        else:
            studentCount[i.courseName] = studentCount[i.courseName] + 1
    print("inside of getTotalStudentCount function")
    print(studentCount)
    return studentCount


def getStudentsEnrolledDictionary(inputCourseList, overallCourses):
    if ((inputCourseList==None) or (overallCourses==None)):
        return {}
    personalDict = {}
    returnDict = {}
    for course in inputCourseList:
        if course.courseName not in personalDict:
            personalDict[course.courseName] = 1
        else:
            personalDict[course.courseName] = personalDict[course.courseName] + 1

    for course in overallCourses:
        if course.courseName in personalDict:
            if course.courseName not in returnDict:
                returnDict[course.courseName] = 1
            else:
                returnDict[course.courseName] = returnDict[course.courseName] + 1
    return returnDict


# Dashboard Page for Professor
@app.route("/ProfessorDashboard")
@login_required
def ProfessorDash():
    user = current_user
    userFullName = user.name
    userType = user.accountType
    # if we are loggin in, but they try to get access to teach portal
    if userType != 'professor':
        # redirect the non-professor account to the student dash
        flash("Students not allowed to acess professor page")
        return redirect(url_for('StudentDash'))
    
    # grab all the courses in the database
    courses = Course.query.order_by(Course.courseName)
    
    # Grab all the courses from the database that professor teaches
    personalCourses = Course.query.filter_by(professor=userFullName).all()
    
    #a function to count all the number of students enrolled in each class
    studentCount = getStudentsEnrolledDictionary(personalCourses, courses)


    # an array of all the classes (even if the professor isn't in it, and there are no duplicates)
    professorCoursesSet = set()
    professorCourseArray = []
    for c in personalCourses:
        if c.courseName not in professorCoursesSet:
            professorCoursesSet.add(c.courseName)
            professorCourseArray.append(c)
    
    return render_template("TeacherDashboard.html", 
                           fullName=current_user.name,
                           courses = professorCourseArray,
                           courseDict = studentCount)


@app.route("/StudentInfo/<course_name>")
@login_required
def StudentInfo(course_name):
    # Get all the students in the given course name
    students = Course.query.filter_by(courseName=course_name).all()
    
    return render_template("StudentInfo.html",
                           fullName=current_user.name,
                           courses=students, 
                           course_name=course_name)


@app.route("/edit", methods=['POST', 'GET'])
@login_required
def edit():
    #collect the data from the form
    first_name = request.form.get('editStudent')
    new_grade = request.form.get('editGrade')
    course_name = request.form.get('course_name')
    
    #find the student in the database based on the course name and student name
    student = Course.query.filter_by(courseName=course_name, student=first_name).first()
    
    #if the student exists, update the grade
    if student:
        student.studentGrade = new_grade
        db.session.commit()
    
    return redirect(url_for('StudentInfo', course_name=course_name))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
