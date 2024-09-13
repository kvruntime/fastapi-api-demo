from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from pathlib import Path

import prisma_init

# from routes.commands import command_router
# from routes.blogs import blogs_router
from routes.posts import post_router
from oauth.route import oauth_router

app = FastAPI(
    title="fastapi-demo",
    summary="lorem ipsum dolor aimet.",
    description=Path(__file__)
    .parent.joinpath("public/description")
    .read_text(encoding="utf-8"),
    version="1.0.0",
    lifespan=prisma_init.api_lifespan,
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(oauth_router)
app.include_router(post_router)


@app.get("/")
def index() -> str:
    return "Working..."
