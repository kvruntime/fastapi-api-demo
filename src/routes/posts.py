import typing

from fastapi import APIRouter, Depends, Request, responses, status

from dtos import PostCreateDto, PostUpdateDto
from prisma.models import Post
from usecases.post_usecase import PostUseCase

post_router = APIRouter(
    prefix="/api/posts", tags=["Posts"], dependencies=[Depends(PostUseCase)]
)
use_case = PostUseCase()


@post_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Get all posts",
    response_model=typing.List[Post],
)
async def get_posts(use_case: typing.Annotated[PostUseCase, Depends(PostUseCase)]):
    return await use_case.get_all_post()


@post_router.get("/{id}", status_code=status.HTTP_200_OK, name="get_post")
async def get_post(id: str):
    return await use_case.get_post_by_id(id)


@post_router.delete("/{id}")
async def delete_post(id: str):
    result = await use_case.delete_post_by_id(id)
    if not result:
        return responses.Response(status_code=status.HTTP_404_NOT_FOUND)
    return responses.Response(status_code=status.HTTP_204_NO_CONTENT)


@post_router.put("/{id}")
async def put_post(id: str, dto: PostUpdateDto):
    post = await use_case.update_post(id, dto)
    if not post:
        return responses.Response(status_code=status.HTTP_404_NOT_FOUND)
    return responses.Response(status_code=status.HTTP_204_NO_CONTENT)


@post_router.patch("/{id}")
async def patch_post():
    return


@post_router.post("/")
async def post_post(
    request: Request,
    dto: PostCreateDto,
    use_case: typing.Annotated[PostUseCase, Depends(PostUseCase)],
):
    post = await use_case.create_new_post(dto)
    return responses.RedirectResponse(
        request.url_for("get_post", id=post.id), status.HTTP_303_SEE_OTHER
    )
