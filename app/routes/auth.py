from flask import Blueprint, render_template, redirect, session, request, flash, url_for
from .. import db
from werkzeug.security import generate_password_hash
from ..models import *
import datetime as dt

# making blueprint
auth_ = Blueprint("auth", __name__, url_prefix='/auth')


# registration 
@auth_.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and request.form['usertype'] == 'admin':
        # check for username
        user = Admins.query.filter_by(username=request.form['username']).first()
        if user:
            flash(message="User with the same username already exists.",category="danger")
            return redirect(url_for('auth.register'))
        
        # check for email
        user = Admins.query.filter_by(email=request.form['email']).first()
        if user:
            flash(message="Email already used.", category="danger")
            return redirect(url_for("auth.register"))
        
        else:
            user = Admins(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password'],
                create_time=str(dt.datetime.now().timestamp())
            )
            db.session.add(user)
            db.session.commit() 

            session['username'] = user.username
            session['usertype'] = "admin"
            flash(message="Registration succesfull redirecting to Dashboard.", category='success')
            return redirect(url_for("admin.dashboard"))

    elif request.method == 'POST' and request.form['usertype'] == 'influencer':
        return str(request.form)
    

    elif request.method == 'POST' and request.form['usertype'] == 'sponcer':
        return str(request.form)
    

    elif request.method == "POST":
        flash("Unidentified request", "alert")
        return redirect(url_for('auth.register'))

    # otherwise return register page.
    return render_template("pages/register.html")




# login page
@auth_.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('pages/login.html')
    else:
        # progressing
        if request.form['user-type'] == 'admin':
            user = db.session.execute(select(Admins).where(Admins.email == request.form['email'] and \
            Admins.password == generate_password_hash(request.form['password'])))

            if user:
                return render_template("/pages/admin/dashboard.html")
            else:
                flash("Credentails miss matched.")

        else:
            return render_template("error.html")