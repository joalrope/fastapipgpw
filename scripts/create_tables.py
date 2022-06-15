from models.user import User
from models.quiz import Quiz
from models.option import Option
from models.reply import Reply
from utils.db import db


def create_tables():
    with db:
        db.create_tables([User, Quiz, Option, Reply])
