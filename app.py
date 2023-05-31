from fastapi_offline import FastAPIOffline
from tortoise.contrib.fastapi import register_tortoise
from pathlib import Path
import dbdomain
from routes.commands import command_router
from routes.blogs import blogs_router

app = FastAPIOffline(
    title="fastapi-demo",
    description=Path("./public/description").read_text(encoding="utf-8"),
    version="1.0.0"
)

app.include_router(command_router)
app.include_router(blogs_router)

@app.get("/")
def index() -> str:
    return "Hello Guys"

register_tortoise(
    app,
    dbdomain.TORTOISE_ORM_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True
)