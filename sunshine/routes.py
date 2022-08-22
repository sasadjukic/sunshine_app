
from sunshine import app, db, MONTHS, DAYS, KEY
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sunshine.models import Users
from sunshine.forms import RegisterForm, UpdateForm, LoginForm
from sunshine.api_calls import (info_home, info_city_one, info_city_two, info_city_three,
                               three_day_info, three_day_forecast, sort_calendar)

@app.route('/')
def home():
    home = info_home('New York', 'temp_c')
    city_one = info_city_one('Amsterdam', 'temp_c')
    city_two = info_city_two('Los Angeles', 'temp_c')
    city_three = info_city_three('Tokyo', 'temp_c')
    return render_template('index.html',
                           key = KEY,
                           months = MONTHS,
                           days = DAYS,
                           location = home[0],
                           time = home[1],
                           month = home[2],
                           day = home[3],
                           h_icon = home[4],
                           h_temp = home[5],
                           c_one_icon = city_one[1],
                           c_one_temp = city_one[2],
                           c_two_icon = city_two[1],
                           c_two_temp = city_two[2],
                           c_three_icon = city_three[1],
                           c_three_temp = city_three[2])

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data 
        password = generate_password_hash(form.password.data, method = 'sha256') 
        home_city = form.home_city.data 
        favorite_city_one = form.favorite_city_one.data 
        favorite_city_two = form.favorite_city_two.data 
        favorite_city_three = form.favorite_city_three.data 
        temperature = form.temperature.data 
        new_user = Users(username = username, password = password,
                         home_city = home_city, favorite_city_one = favorite_city_one,
                         favorite_city_two = favorite_city_two, favorite_city_three = favorite_city_three,
                         temperature = temperature)
        print(new_user)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))

        except:
            return 'Error adding a user'

    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username = form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
        
        else:
            return 'Invalid username or password'

    return render_template('login.html', form = form)

@app.route('/dashboard')
@login_required
def dashboard():

    if current_user.temperature == 'C':
        temp = 'temp_c'
        value = 'celsius'
    else:
        temp = 'temp_f'
        value = 'fahrenheit'

    home = info_home(current_user.home_city, temp)
    city_one = info_city_one(current_user.favorite_city_one, temp)
    city_two = info_city_two(current_user.favorite_city_two, temp)
    city_three = info_city_three(current_user.favorite_city_three, temp)
    
    return render_template('dashboard.html',
                           key = KEY, 
                           months = MONTHS,
                           days = DAYS,
                           value = value,
                           location = home[0],
                           time = home[1],
                           month = home[2],
                           day = home[3],
                           h_icon = home[4],
                           h_temp = home[5],
                           c_one_icon = city_one[1],
                           c_one_temp = city_one[2],
                           c_two_icon = city_two[1],
                           c_two_temp = city_two[2],
                           c_three_icon = city_three[1],
                           c_three_temp = city_three[2])

@app.route('/update', methods = ['GET', 'POST'])
@login_required
def update_user_data():
    form = UpdateForm()

    user = Users.query.filter_by(username=current_user.username).first()

    if form.validate_on_submit():
        user.home_city = form.home_city.data 
        user.favorite_city_one = form.favorite_city_one.data 
        user.favorite_city_two = form.favorite_city_two.data 
        user.favorite_city_three = form.favorite_city_three.data 
        user.temperature = form.temperature.data

        try: 
            db.session.commit()
            return redirect(url_for('dashboard'))

        except:
            return 'Error updating user preferences'

    return render_template('update.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.route('/forecast', methods = ['POST'])
def forecast():
    search = request.form['field']

    if current_user.is_authenticated:
        if current_user.temperature == 'C':
            temp = 'temp_c'
            maxtemp = 'maxtemp_c'
            mintemp = 'mintemp_c'
            value = 'celsius'
        else:
            temp = 'temp_f'
            maxtemp = 'maxtemp_f'
            mintemp = 'mintemp_f'
            value = 'fahrenheit'
    else:
        temp = 'temp_c'
        maxtemp = 'maxtemp_c'
        mintemp = 'mintemp_c'
        value = 'celsius'

    city = three_day_info(search, temp)
    city_forecast = three_day_forecast(search, maxtemp, mintemp)
    calendar = sort_calendar()

    return render_template('forecast.html',
                            value = value,
                            updated_location = city[0],
                            l_time = city[1],
                            l_month = city[2],
                            l_day = city[3],
                            l_icon = city[4],
                            l_temp = city[5],
                            wind_speed = city[6],
                            air_pressure = city[7],
                            humidity = city[8],
                            day_one_f = city_forecast[0],
                            day_one_h = city_forecast[1],
                            day_one_l = city_forecast[2],
                            day_two_f = city_forecast[3],
                            day_two_h = city_forecast[4],
                            day_two_l = city_forecast[5],
                            day_three_f = city_forecast[6],
                            day_three_h = city_forecast[7],
                            day_three_l = city_forecast[8],
                            today = calendar[0],
                            tomorrow = calendar[1],
                            after_tomorrow = calendar[2])