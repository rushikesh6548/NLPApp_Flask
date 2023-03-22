from flask import Flask,render_template,request,redirect,session
from myapi import API

apio = API()
app = Flask(__name__)
from db import Database

dbo = Database()


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',title = 'Home')

@app.route('/register')
def register():
    return render_template('register.html',title = 'Register')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')


    response = dbo.insert(name,email,password)
    if response:
        return render_template('/login',message = 'Registration Successfull ! You Can Login Now ! ')
    else:
        return render_template('/register.html',message = 'Email Already Exists' )


@app.route('/sentiment_gui')
def sentiment_gui():
    return render_template('sentiment_gui.html')


@app.route('/login')
def login():
    return render_template('login.html',title = 'Login')


@app.route('/perform_sentiment',methods = ['post'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = apio.sentiment(text)
    print(response)

    return render_template('sentiment_gui.html',response=response)


@app.route('/perform_login',methods = ['post'])
def perform_login():
    email = request.form.get('user_email_login')
    password = request.form.get('user_password_login')

    response = dbo.search(email, password)

    if response == 1 :
        return render_template('main_gui.html')
        # get him to home gui
    else:
        return render_template('login.html',message = 'Wrong Password / Email !')


app.run(debug =True)