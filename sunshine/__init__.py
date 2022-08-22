
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

app = Flask(__name__)

MONTHS = {'01': 'January', '02': 'February', '03':'March',
          '04': 'April', '05': 'May', '06': 'June',
          '07': 'July', '08': 'August', '09': 'September',
          '10': 'October', '11': 'November', '12': 'December'}

DAYS = {0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5:'SAT', 6:'SUN'} 

KEY = os.environ.get('YOUR_API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from sunshine import routes