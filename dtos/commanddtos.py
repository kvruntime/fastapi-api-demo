from pydantic import BaseModel


class CreateCommandDto(BaseModel):
    os: str
    description: str = ""
    args: str


class UpdateCommandDto(BaseModel):
    os: str | None
    description: str | None
    args: str | None
