import datetime

from flask_login import UserMixin
from flask_mongoengine import MongoEngine
from mongoengine import fields

db = MongoEngine()


class User(UserMixin, db.Document):
    """
    用户表
    """
    username = fields.StringField(required=True, max_length=32, unique=True)
    password = fields.StringField(required=True, max_length=256)
    email = fields.StringField(required=True, max_length=64, unique=True)
    description = fields.StringField(max_length=1024, default='')

    date_joined = fields.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return '<User username:%s>' % self.username

    meta = {
        'collection': 'user',
        'indexes': [
            '#username',
            '#email',
        ]
    }
