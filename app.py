from flask import Flask, render_template, request, redirect, url_for, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)
admin = Admin(app, name='Admin', template_mode='bootstrap3')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    accountType = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(120), nullable=False)
    password = None
    
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

# Dashboard Page for Student
@app.route("/StudentDashboard")
def StudentDash():
    return render_template("StudentDashboard.html", fullName="Peter Pan")

# Dashboard Page for Professor
@app.route("/ProfessorDashboard")
def ProfessorDash():
    return render_template("TeacherDashboard.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
