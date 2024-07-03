from flask import Blueprint, render_template, redirect, session
from ..models import *

auth_ = Blueprint("auth", __name__, url_prefix='/auth')

# registration 
@auth_.route('/register')
def register():
    return render_template("pages/register.html")

# login page
@auth_.route('/login')
def login():
    return render_template('pages/login.html')