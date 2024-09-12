import typing
from fastapi import APIRouter, Request, status, Depends
from prisma.models import Post
from usecases.post_usecase import PostUseCase



post_router = APIRouter(prefix="/api/post", tags=["Posts"])

@post_router.get("/", status_code=status.HTTP_200_OK, description="Get all posts", response_model=typing.List[Post])
async def get_posts(use_case:typing.Annotated[PostUseCase, Depends(PostUseCase)]):
    return []


@post_router.get("/{id}",  status_code=status.HTTP_200_OK)
async def get_post():
    return


@post_router.delete("/{id}")
async def delete_post():
    return


@post_router.put("/{id}")
async def put_post():
    return


@post_router.patch("/{id}")
async def patch_post():
    return


@post_router.post("/")
async def post_post(request: Request):
    return
