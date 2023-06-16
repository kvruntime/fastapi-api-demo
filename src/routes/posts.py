from fastapi import APIRouter, Request, status


post_router = APIRouter(prefix="/api/post", tags=["Posts"])


@post_router.get("/", status_code=status.HTTP_200_OK)
async def get_posts():
    return


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
