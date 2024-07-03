import os
from flask import Flask
from flask import render_template
from .models import db
from .routes import auth


def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///db.sqlite3"

    db.init_app(app)

    with app.app_context():
        from .models import Admins
        db.create_all()

    print("database initialized")

    # registering auth.auth_ blueprint to the app
    app.register_blueprint(auth.auth_)


    # a simple page to check server status
    @app.route('/check')
    def message():
        return "<h1>Site is Live...</h1>"

    @app.route('/')
    def home():
        return render_template("pages/home.html")

    return app