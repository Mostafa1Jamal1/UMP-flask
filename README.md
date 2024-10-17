# UMP Flask

UMP Flask is a user management package built with Flask and MongoDB using MongoEngine. It integrates Flask-Security for user authentication and role management, providing a robust solution for handling user accounts, roles, and permissions.

## Project Structure

```
UMP_flask/
├── __init__.py
├── configuration.py
├── models.py
├── templates
│   └── security
│       └── default.html
└── views.py
```

### Modules

- `__init__.py`: Initializes the application and exports the necessary components.
- `configuration.py`: Contains the configuration settings for the Flask application, including security and mail settings.
- `models.py`: Defines the database models for users and roles using MongoEngine.
- `views.py`: Sets up the application routes using Flask's Blueprint.
- `templates/security/default.html`: Default HTML template extending the base security template.

## Requirements

the following packages are recommended:

- `Flask`: Web framework for Python.
- `Flask-Security`: Provides security features for Flask applications.
- `MongoEngine`: ODM for MongoDB.
- `Flask-Mailman`: Provides email functionality.
- `python-dotenv`: For loading environment variables from a `.env` file.

## Configuration

To set up your application, create a `.env` file in the root directory and define the following variables:

```plaintext
DEBUG=True
SECRET_KEY=your_secret_key
SECURITY_PASSWORD_SALT=your_security_password_salt
MAIL_SERVER=smtp.yourmailserver.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email_username
MAIL_PASSWORD=your_email_password
DB_NAME=mydatabase
```

## Usage Example

You can run the application as follows:

```python
from UMP_flask import configure_app
from flask import Flask

if __name__ == '__main__':
    # run application (can also use flask run)
    app = Flask(__name__)
    configure_app.basic_auth(app=app, debug=True, SECURITY_REGISTERABLE=True)
    configure_app.with_mail(app=app, SECURITY_CONFIRMABLE=True, SECURITY_RECOVERABLE=True, SECURITY_CHANGEABLE=True)
    security = configure_app.security(app=app)
    
    # Run Flask
    app.run()
```

## Features

- User registration and login.
- Email confirmation and password recovery.
- Role-based access control.
- Customizable email settings.
- Easy integration with existing Flask applications.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature requests or bugs you encounter.

## License

This project is licensed under the MIT License.
```

Feel free to customize any sections or details according to your project needs!