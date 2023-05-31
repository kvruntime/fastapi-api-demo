from typing import List
from uuid import UUID
from fastapi import APIRouter, Request, status
from dbdomain.models import Command
from dtos.commanddtos import CreateCommandDto, UpdateCommandDto, ReadCommandDto
from shared.commonrepo import CommonRepo
from fastapi.responses import RedirectResponse, Response, JSONResponse
from tortoise.exceptions import DoesNotExist

command_repo = CommonRepo[Command](Command)

command_router = APIRouter(prefix="/api/commands", tags=["Commands"])


@command_router.get("/", response_model=List[ReadCommandDto], status_code=status.HTTP_200_OK)
async def get_commands():
    _items = await command_repo.read_all()
    return _items


@command_router.get("/{id}", response_model=ReadCommandDto, status_code=status.HTTP_200_OK)
async def get_command(id: UUID):
    try:
        _item = await command_repo.read(id)
        return _item
    except DoesNotExist:
        return Response(
            content=f"Command with id:{id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


@command_router.delete("/{id}")
async def delete_command(id: UUID):
    try:
        await command_repo.delete(id)
    except DoesNotExist:
        return Response(
            content=f"Command with id:{id} not found",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@command_router.put("/{id}")
async def put_command(id: UUID, command: UpdateCommandDto):
    # FIXME: this is the first way (use update function from repository)
    # await command_repo.update(id, Command(**command.dict()))
    try:
        _item = await command_repo.read(id)
        await _item.update_from_dict(command.dict(exclude_unset=True))
        await command_repo.save(_item)
        return Response(content="updated", status_code=status.HTTP_204_NO_CONTENT)
    except DoesNotExist:
        return Response(
            content=f"Command with id:{id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


@command_router.patch("/{id}")
async def patch_command(id: UUID, command: UpdateCommandDto):
    try:
        _item = await command_repo.read(id)
        await _item.update_from_dict(command.dict(exclude_unset=True, exclude_defaults=True))
        await command_repo.save(_item)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except DoesNotExist:
        return Response(
            content=f"Command with id:{id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


@command_router.post("/")
async def post_command(request: Request, command: CreateCommandDto):
    try:
        _item = await command_repo.insert(Command(**command.dict()))
        return RedirectResponse(
            request.url_for("get_command", **dict(id=_item.id)),
            status_code=status.HTTP_303_SEE_OTHER
            # without 303, this wont go to the specified route
        )
    except:
        return Response(content="Invalid credential", status_code=status.HTTP_400_BAD_REQUEST)
