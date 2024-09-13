# coding:utf-8

from pydantic import BaseModel


class PostCreateDto(BaseModel):
    title: str
    content: str


class PostUpdateDto(PostCreateDto):
    title: str = ""
    content: str = ""
    published: bool = False
