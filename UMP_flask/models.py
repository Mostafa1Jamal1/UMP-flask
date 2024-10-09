from mongoengine.fields import (
    BinaryField,
    BooleanField,
    DateTimeField,
    IntField,
    ListField,
    ReferenceField,
    StringField,
)
from mongoengine import Document
from flask_security import UserMixin, RoleMixin
from os import environ


db_name = environ.get("DB_NAME", "mydatabase")

class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)
    permissions = ListField(required=False)
    meta = {"db_alias": db_name}

class User(Document, UserMixin):
    email = StringField(max_length=255, unique=True)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    fs_uniquifier = StringField(max_length=64, unique=True)
    confirmed_at = DateTimeField()
    roles = ListField(ReferenceField(Role), default=[])
    meta = {"db_alias": db_name}


