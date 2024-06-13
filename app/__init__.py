import os
from flask import Flask
from . import db
from . import auth



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    # resgistering db functionality
    db.init_app(app=app)

    # registering auth.Auth blueprint to the app
    app.register_blueprint(auth.Auth)

    # a simple page to check server status
    @app.route('/check')
    def message():
        return "<h1>Site is Live...</h1><p>this is demo paragraph</p>"

    return app