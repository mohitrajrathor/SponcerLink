from functools import wraps
import logging
from flask import Blueprint, session, url_for, redirect, render_template, request, flash, abort
from ..models import Sponcers, Campaigns
import datetime as dt

sponcer = Blueprint('sponcer', __name__, url_prefix='/sponcer')


# decorators for handling auth and usertype 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to log in first.')
            return redirect(url_for('auth.login', usertype='sponcer', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# this page is same as profile page
@sponcer.route('<string:username>/dashboard')
def dashboard(username):
    try:
        # retriving user info
        user = Sponcers.query.filter_by(username=username).first()

        # gathering campaigns info
        camps = user.campaigns
        reqs = user.requests

        # convert camps post_time to date
        if camps:
            for camp in camps:
                camp.post_time = dt.datetime.fromisoformat(camp.post_time).strftime("%b %d, %Y")
                camp.start_date = dt.datetime.fromisoformat(camp.start_date).strftime("%b %d, %Y")
                camp.end_date = dt.datetime.fromisoformat(camp.end_date).strftime("%b %d, %Y")

        if reqs:
            for req in reqs:
                req.req_time = dt.datetime.fromisoformat(req.req_time).strftime("%b %d, %Y")


    except Exception as e:
        logging.warning(f"error while retriving user info ERROR : {e}")
        print(e)
        return abort(404)

    # managing parameter to be passed into template
    params = {
        'username' : username,
        'user' : user,
        'joined_date' : dt.datetime.fromisoformat(user.joined_time).strftime("%b %d, %Y"),
        'campaigns' : camps,
        'adRequests' : reqs
    }

    return render_template('pages/sponcer/dashboard.html', **params)


@sponcer.route('<string:username>/dashboard/campaigns')
@login_required
def campaigns(username):
    return render_template('pages/sponcer/campaigns.html', username=username)


@sponcer.route('<string:username>/dashboard/find')
def find(username):
    return render_template('pages/sponcer/find.html', username=username)
    

@sponcer.route('<string:username>/dashboard/statistics')
def statistics(username):
    return render_template('pages/sponcer/statistics.html', username=username)

