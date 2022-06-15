from datetime import datetime

import peewee

from utils.db import db


class Reply(peewee.Model):
    title = peewee.CharField()
    value = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db