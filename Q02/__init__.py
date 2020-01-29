from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        # Imports
        from . import routes
        db.create_all()

        from .cli import populate_table
        app.cli.add_command(populate_table)

    from .api.users.routes import api
    app.register_blueprint(api)

    return app
