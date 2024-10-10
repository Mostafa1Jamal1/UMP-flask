# UMP-flask

# MUST have .env file
content example:
```# this file should be pretty safe

DEBUG = 'True'

# Generate your own secrete key in the terminal by
# $ python -c 'import secrets; print(secrets.token_hex())'
# 0d31fa3fc57b1edafaa5abf6a7da08917ce86806876373b3933507c
SECRET_KEY = '0d31fa3fc57b1edafaa5abf6a7da08917ce86806876373b3933507c'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'my_account@gmail.com'
MAIL_PASSWORD = 'get_it_from_smtp_provider'
MAIL_USE_TLS = 'False'
MAIL_USE_SSL = 'True'

DATABASE_NAME = 'mydatabase'
```
