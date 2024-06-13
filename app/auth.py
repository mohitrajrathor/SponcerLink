import functools
from flask import Blueprint, g, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

# initializing Blueprint to handle authorization functionality of the app
Auth = Blueprint('auth', __name__, url_prefix='/auth')


@Auth.route('/register', methods=['GET', 'POST'])
def register():
    return 'Registration page...'