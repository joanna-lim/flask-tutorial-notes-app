from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    
    if '@' not in email or ' ' in email[:-1]:
        flash('your email looks wrong :(', category='error')
        
    elif len(firstName) < 2:
        flash('your first name is longer than this, right?', category='error')
        
    elif password1!=password2:
        flash('passwords don\'t match :(', category='error')
        
    elif len(password1) < 8:
        flash('password should be at least 8 characters!', category='error')
        
    else:
        # add user to database
        flash('congrats! account created :)', category='success')
        
    return render_template("sign_up.html")
