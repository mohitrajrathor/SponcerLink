import functools
from flask import Blueprint, render_template, redirect, session, request, flash, url_for
from .. import db
from werkzeug.security import generate_password_hash
from ..models import *
import datetime as dt


# making blueprint
auth_ = Blueprint("auth", __name__, url_prefix='/auth')


# handling login requirement at different level
def specific_login_required(usertype=None):
    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if usertype is None:
                flash("Session expired, please login again.")
                return redirect(url_for('auth.login'))
            
            if 'usertype' not in session:
                flash("Please login.")
                return redirect(url_for('auth.login'))
            
            elif session['usertype'] != usertype:
                flash("Access Prohabited!")
                return redirect(url_for("home"))

            return view(**kwargs)
        return wrapped_view
    return login_required

# registration 
@auth_.route('/register', methods=['GET', 'POST'])
def register():
    next_url = request.args.get('next')
    if request.method == 'POST' and request.form['usertype'] == 'influencer':
        pass
    
    elif request.method == 'POST' and request.form['usertype'] == 'sponcer':
        pass
    
    elif request.method == "POST":
        flash("Unidentified request", "alert")
        return redirect(url_for('auth.register'))

    # otherwise return register page.
    return render_template("pages/register.html")


# login logic
@auth_.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['usertype'] == 'sponcer':
        pass
    elif request.method == 'POST' and request.form['usertype'] == 'influencer':
        pass
    return render_template("pages/login.html")
        

# logout 
@auth_.route("/logout")
def logout():
    session.pop('username')
    session.pop('usertype')
    return redirect(url_for("home"))