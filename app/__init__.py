import os
from flask import Flask
from flask import render_template
import datetime as dt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

    db.init_app(app)

    with app.app_context():
        from .models import Admins #, Industries, Influencers, Sponcers, SocialAccounts, SocialPlatforms, SponcershipRequests, AdRequests, Campaigns, Categories
        db.create_all()

    print("database initialized")

    # registering auth.auth_ blueprint to the app
    from .routes import auth, admin
    app.register_blueprint(auth.auth_)
    app.register_blueprint(admin.admin)


    # a simple page to check server status
    @app.route('/check')
    def check():
        return "<h1>Site is Live...</h1>"


    @app.route('/404')
    def _404():
        return render_template('pnf.html')

    @app.route('/')
    def home():
        return render_template("pages/home.html")

    return app
