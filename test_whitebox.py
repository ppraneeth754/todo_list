import os
# os.environ['DATABASE_URL'] = 'sqlite:///app.db'  # use an in-memory database for tests

import unittest
from flask import current_app
# from app import app
import requests
from subpython import validate
from subpython.form import LoginForm , RegisterForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask,render_template ,redirect 
from flask_session import Session


url = '127.0.0.1:5000'

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

db_path = os.path.join(os.path.dirname(__file__),'app.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64) ,nullable=False ,unique=True)
    password = db.Column(db.String(256) ,nullable=False,unique=False)
    # 0 = New user || 1 = Old User
    new_user = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime ,default=datetime.now())

class TestWebApp(unittest.TestCase):
		## Initial Page api testing
		def test_home_page_redirect(self):
			# response = app.get('/login', follow_redirects=True)
			response = requests.get('http://127.0.0.1:5000')
			# print(response.content)
			print("Home page Module Testing")
			assert response.status_code == 200
			assert "Login" in str(response.content)

	   
		def test_validate_passwords(self):
			# print("Testing User password")
			user_password = 'Test1234'
			saved = 'Test1234'
			test_resp = validate.validate_passwords(user_password,saved)
			print("\nRight Password", test_resp)
			assert test_resp == True
			
		def test_validate_passwords2(self):
			saved = 'Test1234'
			user_password = 'Check1234'
			test_resp = validate.validate_passwords(user_password,saved)
			print("\nWrong Password", test_resp)
			assert test_resp != True


		def test_username_validation(self):
			username = 'test'
			print("\nusername Validation", username)
			# print(username)
			assert validate.validate_field(username) == True
			
		def test_username_validation2(self):
			username = 'test_@#'
			print("\nusername Validation", username)
			assert validate.validate_field(username) != True
		
		def test_password_validate(self):
			print("\nPassword Validation")
			password = 'Test1234'
			assert validate.validate_field(password) == True	




if __name__ == '__main__':
	unittest.main()