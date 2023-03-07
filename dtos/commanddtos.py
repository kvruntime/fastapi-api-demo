from pydantic import BaseModel


class CreateCommandDto(BaseModel):
    os: str
    description:str = ""
    args: str


class UpdateCommandDto(CreateCommandDto):
    pass
