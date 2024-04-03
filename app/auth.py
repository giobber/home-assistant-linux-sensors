import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from . import settings

router = APIRouter()

security = HTTPBasic()

Credentials = Annotated[HTTPBasicCredentials, Depends(security)]


def check_username(username: str):
    current = username.encode("utf8")
    correct = settings.USERNAME.encode("utf8")
    return secrets.compare_digest(current, correct)


def check_password(password: str):
    current = password.encode("utf8")
    correct = settings.PASSWORD.encode("utf8")
    return secrets.compare_digest(current, correct)


def check_credentials(credentials: Credentials):
    is_username_valid = check_username(credentials.username)
    is_password_valid = check_password(credentials.password)

    if is_username_valid and is_password_valid:
        return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


Authenticate = Annotated[str, Depends(check_credentials)]


@router.get("/user")
def get_user(username: Authenticate):
    return username


@router.get("/logout")
def logout():
    raise HTTPException(
        status_code=401, detail="Logged out", headers={"WWW-Authenticate": "Basic"}
    )
