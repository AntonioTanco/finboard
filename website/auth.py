from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')

def login():
    return render_template("login.html", test="testing", user="Tim", boolean=False)

@auth.route('/logout')

def logout():
    return render_template()

@auth.route('sign-up')

def signup():
    return render_template("sign-up.html")