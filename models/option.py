from datetime import datetime

import peewee

from utils.db import db
from .reply import Reply


class Option(peewee.Model):
    title = peewee.CharField()
    replies = peewee.ForeignKeyField(Reply, backref="option")
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db
