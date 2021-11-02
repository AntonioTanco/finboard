from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])

def login():
    data = request.form
    print(data)
    return render_template("login.html", test="testing", user="Tim", boolean=False)

@auth.route('/logout')

def logout():
    return render_template()

@auth.route('sign-up', methods=['GET', 'POST'])

def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="Error")
        elif len(firstName) < 2:
            flash("First Name must be greater than 2 characters", category="Error")
        elif password1 != password2:
            flash("Password do not match each other", category="Error")
        elif len(password1) < 7:
            flash("Password must be greater than ", category="Error")
            pass
        else:
            # Add user to a datebase
            pass



    return render_template("sign-up.html")