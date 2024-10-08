from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

    # initialization 
    db.init_app(app)


    with app.app_context():
        from .models import Admins, Industries, Influencers, Sponcers, Campaigns, Niches
        db.create_all()

    print("database initialized")

    # registering routes blueprint to the app
    from .routes import auth, admin, sponcer, influencer
    app.register_blueprint(auth.auth_)
    app.register_blueprint(admin.admin)
    app.register_blueprint(sponcer.sponcer)
    app.register_blueprint(influencer.influencer)

    # registering api blueprint
    from .apis import transaction_apis, request, campaign
    app.register_blueprint(transaction_apis.tranx, url_prefix='/api/transaction')
    app.register_blueprint(request.request_api, url_prefix='/api/request')
    app.register_blueprint(campaign.campaign_api, url_prefix='/api/campaign')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('pnf.html')

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
