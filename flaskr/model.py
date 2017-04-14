from flask_mongoengine import MongoEngine

from mongoengine import fields

db = MongoEngine()


class User(db.Document):
    name = fields.StringField(required=True, max_length=64)
    password = fields.StringField(max_length=256)
    email = fields.StringField(max_length=64)
    description = fields.StringField(max_length=1024)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    # TypeError: ObjectId('552f41e56a85f00dd043406b') is not JSON serializable
    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.name