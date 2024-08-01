from flask import Flask
from flask import Blueprint, session, url_for, redirect, render_template
from .auth import specific_login_required


sponcer = Blueprint('sponcer', __name__, url_prefix='/sponcer')


@sponcer.route('<str:username>/dashboard', methods=['GET'])
def dashboard(username):
    return render_template('pages/sponcer/dashboard.html')