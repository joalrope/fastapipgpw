import email
from fastapi import HTTPException, status

from models.user import User as UserModel
from schemas import user as user_schema

from services.auth import get_password_hash


def create_user(user: user_schema.UserRegister):

    get_user: user_schema.UserRegister = UserModel.filter((UserModel.email == user.email) | (
        UserModel.username == user.username)).first()

    email_msg = ""
    user_msg = ""
    cnn_msg = ""

    if get_user:
        if get_user.email == user.email:
            email_msg = "Email "

        if get_user.username == user.username:
            user_msg = "Username "

        if email_msg & user_msg:
            cnn_msg = "and "

        msg = f"{email_msg}{cnn_msg}{user_msg}already registered"

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id=db_user.id,
        username=db_user.username,
        email=db_user.email
    )
