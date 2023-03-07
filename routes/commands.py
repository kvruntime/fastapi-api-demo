from uuid import UUID
from fastapi import APIRouter, Request
from dbdomain.models import Command
from dtos.commanddtos import CreateCommandDto, UpdateCommandDto
from shared.commonrepo import CommonRepo
from fastapi.responses import RedirectResponse

command_repo = CommonRepo[Command](Command)

command_router = APIRouter(prefix="/api/commands", tags=["Commands"])


@command_router.get("/")
async def get_commands():
    return await command_repo.read_all()


@command_router.get("/{id}")
async def get_command(id: UUID):
    return await command_repo.read(id)


@command_router.delete("/{id}")
async def delete_command(id: UUID):
    await command_repo.delete(id)
    return None


@command_router.put("/{id}")
async def put_command(id: UUID, command: UpdateCommandDto):
    # FIXME: this is the first way (use update function from repository)
    # await command_repo.update(id, Command(**command.dict()))

    _item = await command_repo.read(id)
    await _item.update_from_dict(command.dict(exclude_unset=True))
    await command_repo.save(_item)
    return


@command_router.post("/")
async def post_command(request: Request, command: CreateCommandDto):
    _item = await command_repo.insert(Command(**command.dict()))
    return RedirectResponse(request.url_for("get_command", **dict(id=_item.id)), status_code=303)
