# from UMP_flask import configure_app
from UMP_flask import configure_app
from flask import Flask


if __name__ == '__main__':
    # run application (can also use flask run)
    app = Flask(__name__)
    configure_app.basic_auth(app=app, debug=True,
                             SECURITY_REGISTERABLE=True)
    configure_app.with_mail(app=app,
                            SECURITY_SEND_REGISTER_EMAIL=True,
                            SECURITY_CONFIRMABLE=True,
                            SECURITY_RECOVERABLE=True,
                            SECURITY_CHANGEABLE=True)
    security = configure_app.security(app=app)
    # Run Flask
    app.run()
