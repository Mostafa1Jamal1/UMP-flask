# UMP_flask

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Configuration](#configuration)
   - [Example .env File](#example-env-file)
4. [Basic Usage](#basic-usage)
5. [Advanced Usage](#advanced-usage)
6. [API Documentation](#api-documentation)
   - [configure_app Class](#configure_app-class)
   - [Error Handling](#error-handling)
7. [Deployment Considerations](#deployment-considerations)
8. [Testing](#testing)
9. [Contributions](#contributions)
10. [License](#license)

--- 

## Project Overview

**UMP_flask** is a Python-based package designed to simplify and speed up the development of user management systems, a core feature in most applications. This package leverages Flask, Flask-Security, and other libraries, offering developers a flexible framework to handle user authentication, roles, permissions, and more.

### Purpose
This package is the culmination of my graduation project from the ALX program. It is designed to streamline the process of building user management systems, allowing developers to focus on building their applications while UMP_flask takes care of the essentials like user authentication, password management, and more.

### Core Features
- User authentication with Flask-Security
- Role and permission management
- Mail configuration for password recovery and account confirmation
- Database flexibility with MongoDB (via MongoEngine)
- Easy to configure and extend with environment variables

**Planned Future Features:**
- Authorization with social platforms (OAuth)

---

## Installation

To install the UMP_flask package, you can use `pip`:

```bash
pip install UMP_flask
```

---

## Configuration

UMP_flask requires certain configurations to function properly. You will need to provide a `.env` file with the following configurations:

### Example `.env` file:

```dotenv
SECRET_KEY=your_secret_key_here
SECURITY_PASSWORD_SALT=your_password_salt_here

MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_email_password

DB_NAME=mydatabase
```

At a minimum, you must provide `SECRET_KEY` and `SECURITY_PASSWORD_SALT`. These are essential for Flask-Security's authentication mechanisms. If you're using the mail functionalities, you also need to configure the `MAIL_*` settings. Similarly, don't forget to set up the database (`DB_NAME`).

Generate your own `SECRET_KEY` in the terminal by

```bash
$ python -c 'import secrets; print(secrets.token_hex())'
0d31fa3fc57b1edafaa5abf6a7da08917ce86806876373b3933507c804e905d6
```

Generate your own password salt by

```bash
$ python3 -c 'import secrets; print(secrets.SystemRandom().getrandbits(128))'
142886499610136563183651144257829073709
```

---

## Basic Usage

Here's how you can use UMP_flask in your project:

```python
from UMP_flask import configure_app
from flask import Flask

if __name__ == '__main__':
    # Initialize Flask app
    app = Flask(__name__)

    # Configure the app with basic auth and mail settings
    configure_app.basic_auth(app=app,
                             debug=True,
                             SECURITY_REGISTERABLE=True)
    configure_app.with_mail(app=app,
                            SECURITY_CONFIRMABLE=True,
                            SECURITY_RECOVERABLE=True,
                            SECURITY_CHANGEABLE=True)

    # Set up Flask-Security
    security = configure_app.security(app=app)

    # Run the app
    app.run()
```

This example demonstrates initializing the Flask app with basic authentication and mail configuration for user confirmation and password recovery features.

---

## API Documentation

### `configure_app` Class

The `configure_app` class provides methods to configure and initialize various parts of your application. Here’s a breakdown of its core methods:

1. **`basic_auth(app: Flask, debug: Optional[bool] = False, SECURITY_REGISTERABLE: Optional[bool] = False) -> Flask`**
   - Configures the basic authentication settings for your Flask app.
   - Takes optional parameters for enabling debug mode and user registration.
   - Example usage:
     ```python
     configure_app.basic_auth(app=app, debug=True, SECURITY_REGISTERABLE=True)
     ```

2. **`with_mail(app: Flask, SECURITY_CONFIRMABLE: Optional[bool] = False, SECURITY_RECOVERABLE: Optional[bool] = False, SECURITY_CHANGEABLE: Optional[bool] = False) -> Flask`**
   - Sets up mail-related configurations such as account confirmation, password recovery, and changeability.
   - Example usage:
     ```python
     configure_app.with_mail(app=app, SECURITY_CONFIRMABLE=True)
     ```

3. **`security(app: Flask) -> Security`**
   - Initializes Flask-Security by setting up the user data store and connecting it to MongoDB.
   - Example usage:
     ```python
     security = configure_app.security(app=app)
     ```

### Error Handling
Make sure your `.env` file contains all the required configurations. If any key variables like `SECRET_KEY` or `SECURITY_PASSWORD_SALT` are missing, the app will raise an exception with a clear error message.

---

## Deployment Considerations

When deploying this package, ensure that all necessary configurations (such as `SECRET_KEY` and `MAIL_SERVER`) are correctly set up. It's also a good idea to test your mail server configuration using tools like [GMass](https://www.gmass.co/smtp-test) or any other SMTP testing tools to ensure everything is working as expected.

---

## Advanced Usage

Because UMP_flask builds on top of Flask-Security, it inherits a lot of flexibility in terms of customization. You can extend or modify user management functionalities by using Flask-Security’s configuration options. You can find more detailed documentation on Flask-Security [here](https://flask-security-too.readthedocs.io/en/stable/).

Feel free to add custom authentication flows, password policies, or security measures according to your app's needs.
you can even change the database used by configuring your prefered one which is easy to do with flask-security

---
## Testing

Testing is currently a work in progress. A full test suite will be provided in future releases. Contributions are welcome in this area!

---

## Contributions

Contributions are welcome, whether it's for feature requests, bug fixes, or improving documentation. Below are some suggested areas where contributions would be particularly helpful:
- **Feature Requests:** Implementing new features like social authentication (OAuth).
- **Bug Reports:** Identifying and fixing bugs.
- **Testing:** Writing unit tests, integration tests, and end-to-end tests for the package.
- **Documentation:** Helping to improve and expand the documentation.

If you'd like to contribute, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/Mostafa1Jamal1/UMP-flask/).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---