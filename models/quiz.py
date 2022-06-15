from datetime import datetime

import peewee

from utils.db import db
from .user import User
from .option import Option


class Quiz(peewee.Model):
    code = peewee.CharField()
    title = peewee.CharField()
    category = peewee.CharField()
    questions = peewee.ForeignKeyField(Option, backref="quiz")
    created_at = peewee.DateTimeField(default=datetime.now)
    user = peewee.ForeignKeyField(User, backref="quiz")

    class Meta:
        database = db
