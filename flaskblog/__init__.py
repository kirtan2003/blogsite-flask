import os
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager, login_required
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '06fff47fb68f8bebb0fed635951fc817'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
LoginManager = LoginManager(app)
LoginManager.login_view = 'login' 
LoginManager.login_message_category = 'info' 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'noreply@demo.com'
app.config['MAIL_PASSWORD'] = 'Kirttu@123'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)

from flaskblog import routes