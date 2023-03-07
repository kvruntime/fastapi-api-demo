from fastapi_offline import FastAPIOffline
from tortoise.contrib.fastapi import register_tortoise

import dbdomain
from routes.commands import command_router

app = FastAPIOffline()
app.include_router(command_router)

@app.get("/")
def index() -> str:
    return "Hello Guys"

register_tortoise(
    app,
    dbdomain.TORTOISE_ORM_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True
)