from flask import Flask, render_template, request, redirect, url_for, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin, LoginManager, login_required, logout_user, current_user 


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
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    accountType = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True
    def get_id(self):
        return self.username
    def is_authenticated(self):
        return self.authenticated
    def is_anonymous(self):
        return False

    
# only include this Model if we want different tables for Student
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     username = None
#     password = None
# only include this Model if we want different tables for Professor

# class Professor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     username = None
#     password = None


admin.add_view(ModelView(User, db.session))

# Login Page for Student
@app.route("/")
def index():
    return render_template("LoginPage.html")

@app.route("/login/", methods=['POST', 'GET'])
def login():
    requestedData = request.json
    usrName = requestedData['username']
    usrPsswrd = requestedData['password']

    # user = db.session.query(User.id).filter_by(username=usrName).first()
    curUser = User.query.filter_by(username=usrName).first()

    if curUser is not None:
        print("user found")
        print(curUser.accountType)
        if curUser.password == usrPsswrd:
            print("password is a go")
            login
    else:
        print("user not found")

    print(usrName)
    print(usrPsswrd)
    return "hi"

# Dashboard Page for Student
@app.route("/StudentDashboard")
@login_required
def StudentDash():
    return render_template("StudentDashboard.html", fullName="Izaac Ramirez")

# Dashboard Page for Professor
@app.route("/ProfessorDashboard")
def ProfessorDash():
    return render_template("TeacherDashboard.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
