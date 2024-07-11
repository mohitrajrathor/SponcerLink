from flask import render_template, redirect, request, session, url_for, Blueprint
from . import auth
from .. import models, db

admin = Blueprint("admin", __name__, url_prefix="/admin")


auth.login_required(type='admin')
admin.route("/")
admin.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("pages/admin/dashboard")