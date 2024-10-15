"""
UMP Flask Application Configuration

This module provides configuration settings and functions for the UMP Flask application.
"""

from os import environ as env
from dotenv import load_dotenv
from flask import Flask
from mongoengine import connect
from flask_security import (
    Security,
    MongoEngineUserDatastore,
)
from .views import blueprint
from flask_mailman import Mail
from typing import Optional

load_dotenv()


class configure_app():
    def basic_auth(app: Flask,
                   debug: Optional[bool] = False,
                   SECURITY_REGISTERABLE: Optional[bool] = False,
                   ) -> Flask:
        """
        Configure basic auth for the given app.

        Args:
            app: The Flask application instance to configure.
            debug: Whether to enable debug mode for the app.
            SECURITY_REGISTERABLE: Whether to enable user registration.

        Returns:
            The configured app.
        """
        app.config['DEBUG'] = debug or (env.get("DEBUG") == "True")

        # for security these variables should be set in .env
        app.config['SECRET_KEY'] = env.get("SECRET_KEY")
        app.config['SECURITY_PASSWORD_SALT'] = (
            env.get("SECURITY_PASSWORD_SALT").encode("utf-8")
            )
        if not app.config.get('SECRET_KEY'):
            raise Exception("SECRET_KEY is not set in .env file")
        if not app.config.get('SECURITY_PASSWORD_SALT'):
            raise Exception("SECURITY_PASSWORD_SALT is not set in .env file")

        app.config['SECURITY_REGISTERABLE'] = SECURITY_REGISTERABLE
        app.register_blueprint(blueprint)
        return app


    def security(app: Flask) -> Security:
        """
        Create a Flask-Security instance for the given app.

        Args:
            app: The Flask application instance to configure.

        Returns:
            A Flask-Security instance for the given app.
        """
        from .models import User, Role
        db_name = env.get("DB_NAME", "mydatabase")
        db = connect(alias=db_name, db=db_name,
                     host="mongodb://localhost", port=27017)
        # Setup Flask-Security
        user_datastore = MongoEngineUserDatastore(db, User, Role)
        security = Security(app, user_datastore)
        return security
