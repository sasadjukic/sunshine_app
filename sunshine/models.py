from sunshine import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader 
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False, unique = True)
    home_city = db.Column(db.String(30), nullable = False)
    favorite_city_one = db.Column(db.String(30), nullable = False)
    favorite_city_two = db.Column(db.String(30), nullable = False)
    favorite_city_three = db.Column(db.String(30), nullable = False)
    temperature = db.Column(db.String(5), nullable = False)