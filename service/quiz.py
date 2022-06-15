from fastapi import HTTPException, status

from schemas.quiz import QuizCreate
from schemas.quiz import Quiz
from schemas.user import User
from models.quiz import Quiz as QuizModel


def create_task(task: QuizCreate, user: User):

    db_task = QuizModel(
        code=task.code,
        title=task.title,
        category=task.category,
        user_id=user.id
    )

    db_task.save()

    return Quiz(
        id=db_task.id,
        code=db_task.code,
        title=db_task.title,
        category=db_task.category,
        created_at=db_task.created_at
    )
