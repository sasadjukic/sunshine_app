
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SelectField, SubmitField 
from wtforms.validators import DataRequired 

class RegisterForm(FlaskForm):
    temp_choices = ['C', 'F']
    username = StringField(label = 'Username: ', validators = [DataRequired()])
    password = PasswordField(label = 'Password: ', validators = [DataRequired()])
    home_city = StringField(label = 'Home City: ', validators = [DataRequired()])
    favorite_city_one = StringField(label = 'Favorite City 1: ', validators = [DataRequired()])
    favorite_city_two = StringField(label = 'Favorite City 2: ', validators = [DataRequired()])
    favorite_city_three = StringField(label = 'Favorite City 3: ', validators = [DataRequired()])
    temperature = SelectField(label = 'Temperature: ', choices = temp_choices, validators = [DataRequired()])
    submit = SubmitField(label = 'SUBMIT')

class UpdateForm(FlaskForm):
    temp_choices = ['C', 'F']
    home_city = StringField(label = 'Home City: ', validators = [DataRequired()])
    favorite_city_one = StringField(label = 'Favorite City 1: ', validators = [DataRequired()])
    favorite_city_two = StringField(label = 'Favorite City 2: ', validators = [DataRequired()])
    favorite_city_three = StringField(label = 'Favorite City 3: ', validators = [DataRequired()])
    temperature = SelectField(label = 'Temperature: ', choices = temp_choices, validators = [DataRequired()])
    submit = SubmitField(label = 'UPDATE')

class LoginForm(FlaskForm):
    username = StringField(label = 'Username: ', validators = [DataRequired()])
    password = PasswordField(label = 'Password: ', validators = [DataRequired()])
    submit = SubmitField(label = 'SUBMIT')