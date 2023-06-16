# coding:utf-8
import typing
from fastapi import APIRouter, Form
from pydantic import EmailStr


oauth_router = APIRouter(prefix="/api/oauth", tags=["OAuth"])


@oauth_router.post("/signup")
def register_user(
    email: typing.Annotated[EmailStr, Form],
    password: typing.Annotated[str, Form],
    re_password: typing.Annotated[str, Form],
):
    return
