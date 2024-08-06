from flask import render_template, redirect, request, session, url_for, Blueprint, flash
from ..models import Admins
from .. import db

# Constants
SECRET_KEY = "adminchangepassword"


admin = Blueprint("admin", __name__, url_prefix="/admin")


# admin login logic
@admin.route('/auth', methods=['GET', 'POST'])
def login():
    """
    admin login
        param: None

    description: 
        check for given credentials and login admin.
    """
    next_url = request.args.get('next')
    if request.method == 'POST':
        user = Admins.query.filter_by(email=request.form['email'], password=request.form['password']).first()
        if user:
            session['username'] = user.username
            session['usertype'] = 'admin'
            return redirect(next_url or url_for('admin.dashboard', username=user.username))
        else:
            flash("Not a Valid Admin.")
            return redirect(url_for('admin.login'))
        
    if 'usertype' in session and session['usertype'] == 'admin':
        return redirect(url_for("admin.dashboard"))
    
    return render_template('pages/admin/login.html')

# dashboard 
@admin.route("/<username>")
@admin.route("/<username>/dashboard", methods=["GET"])
def dashboard(username):
    return render_template("pages/admin/dashboard.html")