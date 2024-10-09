from os import environ
from flask import Flask
from mongoengine import connect
from flask_security import (
  Security,
  MongoEngineUserDatastore,
)
from UMP_flask import blueprint


def create_app():
  app = Flask(__name__)

  app.config['DEBUG'] = True if environ.get("DEBUG") == "True" else False
  app.config['MAIL_SERVER'] = environ.get("MAIL_SERVER")
  app.config['MAIL_PORT'] = int(environ.get("MAIL_PORT"))
  app.config['MAIL_USE_TLS'] = True if environ.get("MAIL_USE_TLS") == "True" else False
  app.config['MAIL_USE_SSL'] = True if environ.get("MAIL_USE_SSL") == "True" else False
  app.config['MAIL_USERNAME'] = environ.get("MAIL_USERNAME")
  app.config['MAIL_PASSWORD'] = environ.get("MAIL_PASSWORD")
  # Generate a nice key using secrets.token_urlsafe()
  app.config['SECRET_KEY'] = str(environ.get("SECRET_KEY")).encode()
  # Generate a good salt for password hashing using: secrets.SystemRandom().getrandbits(128)
  app.config['SECURITY_PASSWORD_SALT'] = environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')

  app.register_blueprint(blueprint)

  return app




def create_security(app):
  from UMP_flask import User, Role
  # Create database connection object
  db_name = "mydatabase"
  db = connect(alias=db_name, db=db_name, host="mongodb://localhost", port=27017)
  # Setup Flask-Security
  user_datastore = MongoEngineUserDatastore(db, User, Role)
  security = Security(app, user_datastore)
  return security