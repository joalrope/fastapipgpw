from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class QuizBase(BaseModel):
    code: str = Field(
        ...,
        min_length=3,
        max_length=3,
        example="001"
    )
    title: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Basic quiz about you"
    )
    category: str = Field(
        ...,
        min_length=3,
        max_length=15,
        example="Hoobies"
    )


class QuizCreate(QuizBase):
    id: int = Field(
        ...,
        example="5"
    )


class Quiz(QuizCreate):
    id: int = Field(...)
    created_at: datetime = Field(default=datetime.now())
