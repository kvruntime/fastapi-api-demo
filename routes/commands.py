from uuid import UUID
from fastapi import APIRouter, Request, status
from dbdomain.models import Command
from dtos.commanddtos import CreateCommandDto, UpdateCommandDto
from shared.commonrepo import CommonRepo
from fastapi.responses import RedirectResponse, Response
from tortoise.exceptions import DoesNotExist

command_repo = CommonRepo[Command](Command)

command_router = APIRouter(prefix="/api/commands", tags=["Commands"])


@command_router.get("/")
async def get_commands():
    return await command_repo.read_all()


@command_router.get("/{id}")
async def get_command(id: UUID):
    try:
        return await command_repo.read(id)
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
            status_code=status.HTTP_404_NOT_FOUND
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
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except DoesNotExist:
        return Response(
            content=f"Command with id:{id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


@command_router.post("/")
async def post_command(request: Request, command: CreateCommandDto):
    _item = await command_repo.insert(Command(**command.dict()))
    return RedirectResponse(
        request.url_for("get_command", **dict(id=_item.id)),
        status_code=status.HTTP_201_CREATED
    )
