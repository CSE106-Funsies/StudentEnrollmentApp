from flask import Flask, render_template, request, redirect, url_for, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin, LoginManager, login_required, logout_user, current_user, login_user


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
        # return self.username
        return self.id
    def is_authenticated(self):
        return self.authenticated
    def is_anonymous(self):
        return False


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
            curUser.authenticated = True
            db.session.commit()
            login_user(curUser, remember=True)
            # return "hi"
            return redirect(url_for('StudentDash'))
    else:
        print("user not found")
        return False 

    print(usrName)
    print(usrPsswrd)
    return "hi"


@app.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.commit()
    logout_user()
    return render_template('/')

# Dashboard Page for Student
@app.route("/StudentDashboard", methods=['POST', 'GET'])
@login_required
def StudentDash():
    user = current_user
    # print(user)
    userFullName = user.name
    print(userFullName)
    print("kk")
    return render_template("StudentDashboard.html", fullName=userFullName)

# Dashboard Page for Professor
@app.route("/ProfessorDashboard")
def ProfessorDash():
    return render_template("TeacherDashboard.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
