from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from pathlib import Path
from prisma_init import register_prisma
# from routes.commands import command_router
# from routes.blogs import blogs_router


app = FastAPI(
    title="fastapi-demo",
    description=Path("./public/description").read_text(encoding="utf-8"),
    version="1.0.0",
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# app.include_router(command_router)
# app.include_router(blogs_router)


@app.get("/")
def index() -> str:
    return "Hello Guys"


register_prisma(app)
