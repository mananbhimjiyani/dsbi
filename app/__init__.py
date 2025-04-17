from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

# Import models AFTER db initialization
from app.models import User, AdCampaign  # Add this line

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Use from_object instead of from_pyfile

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Add user_loader within app context
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .views.auth import auth_bp
    from .views.main import main_bp
    from .views.admin import admin_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
