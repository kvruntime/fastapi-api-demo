from fastapi import APIRouter, status, Request

blog_router = APIRouter(prefix="/api/blogs", tags=["Blogs"])


@blog_router.get("/", status_code=status.HTTP_200_OK)
async def get_posts():
    return


@blog_router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_post():
    return


@blog_router.delete("/{id}")
async def delete_post():
    return


@blog_router.put("/{id}")
async def put_post():
    return


@blog_router.patch("/{id}")
async def patch_post():
    return


@blog_router.post("/")
async def post_post(request: Request):
    return
