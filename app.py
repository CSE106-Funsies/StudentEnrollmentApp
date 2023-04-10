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

# Create a Form Class

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

    

admin.add_view(ModelView(User, Course, db.session))

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

# Dashboard Page for Student
@app.route("/StudentDashboard", methods=['POST', 'GET'])
@login_required
def StudentDash():
    user = current_user
    # # print(user)
    userFullName = user.name
    print(userFullName)
    # print("kk")
    # return render_template("StudentDashboard.html", fullName="jess")
    return render_template("StudentDashboard.html", fullName=current_user.name)


# Dashboard Page for Professor
@app.route("/ProfessorDashboard")
@login_required
def ProfessorDash():
    user = current_user
    userFullName = user.name
    return render_template("TeacherDashboard.html", fullName=userFullName)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
