import functools
import logging
from flask import Blueprint, render_template, redirect, session, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
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
                flash("Access Prohabited! Reason : <strong>Wrong user</strong>")
                return redirect(url_for("home"))

            return view(**kwargs)
        return wrapped_view
    return login_required

# registration 
@auth_.route('/register/<usertype>', methods=['GET', 'POST'])
def register(usertype):
    next_url = request.args.get('next')

    if usertype=='influencer':
        if request.method == 'GET':
            return render_template('pages/auth_pages/influencer-register.html')
        elif request.method == 'POST':
            user = Influencers(
                username=request.form['username'],
                name=request.form['name'],
                email=request.form['email'],
                password=generate_password_hash(request.form['password']),
                joined_time=str(dt.datetime.now().timestamp())
            )
            try:
                db.session.add(user)
                db.db.session.commit()
                session['usertype'] = 'sponcer'
                session['username'] = user.username
                session['id'] = user.id

            except Exception as e:
                logging.warning(f"error while registering user ERROR : {e}")
                if Influencers.query.filter_by(username=request.form['username']).first():
                    flash('Username already exist choose another username.')
                elif Influencers.query.filter_by(email=request.form['email']).first():
                    flash('Email already used, try different one.')
                else:
                    flash('Invalid credentials.')
                db.session.rollback()
                return redirect(url_for('auth.register', usertype='influencer'))
            
            return redirect(url_for('influencer.dashboard', username=user.username))

    elif usertype == 'sponcer':
        # render sponcer registration page 
        if request.method == 'GET':
            industries = Industries.query.all()
            return render_template('pages/auth_pages/sponcer-register.html', industries=industries)
        elif request.method == 'POST':
            user = Sponcers(
                username=request.form['username'],
                name=request.form['name'],
                company= request.form['company'] if request.form['company'] != '' else None,
                ind_id=request.form['industry'],
                email=request.form['email'],
                password=generate_password_hash(request.form['password']),
                website=request.form['website'] if request.form['website'] != '' else None,
                joined_time=str(dt.datetime.now().timestamp())
            )
            try:
                db.session.add(user)
                db.session.commit()
                session['usertype'] = 'sponcer'
                session['username'] = user.username
                session['id'] = user.id
            except Exception as e:
                logging.warning(f"error while registering user ERROR : {e}")
                if Sponcers.query.filter_by(username=request.form['username']).first():
                    flash('Username already exist choose another username.')
                elif Sponcers.query.filter_by(email=request.form['email']).first():
                    flash('Email already used, try different one.')
                else:
                    flash('Invalid credentials.')
                db.session.rollback()
                return redirect(url_for('auth.register', usertype='sponcer'))

            return redirect(url_for('sponcer.dashboard', username=user.username))
        else:
            flash('Bad Request Method.')
            return redirect(url_for('auth.register', usertype='sponcer'))
    
    elif request.method == "POST":
        flash("Unidentified request", "alert")
        return redirect(url_for('auth.register', usertype='sponcer'))

    # otherwise return register page.
    return redirect(url_for('_404'))



# login logic
@auth_.route('/login/<usertype>', methods=['GET', 'POST'])
def login(usertype):
    next_url = request.args.get('next')
    if request.method == 'GET':
        return render_template(f'pages/auth_pages/{usertype}-login.html')
    elif request.method == 'POST':
        if usertype == 'sponcer':
            try:
                user = Sponcers.query.filter_by(email=request.form['email']).first()
                if check_password_hash(user.password, request.form['password']):
                    session['usertype'] = 'sponcer'
                    session['username'] = user.username
                    session['id'] = user.id
                    
                    return redirect(next_url or url_for('sponcer.dashboard', username=user.username))
                
            except Exception as e:
                print(e)
                db.session.rollback()
                flash('Credentials invalid')
                return redirect(url_for('auth.login', usertype='sponcer'))
            
        elif usertype == 'influencer':
            try:
                user = Influencers.query.filter_by(email=request.form['email']).first()
                if check_password_hash(user.password, request.form['password']):
                    return redirect(next_url or url_for('influencer.dashboard', username=user.username))
            except Exception as e:
                print(e)
                db.session.rollback()
                flash('Credentials invalid')
                return redirect(url_for('auth.login', usertype='influencer'))

    return render_template("pnf.html")
        


# logout 
@auth_.route("/logout")
def logout():
    session.pop('username')
    session.pop('usertype')
    return redirect(url_for("home"))

