from fastapi import APIRouter

blogs_router = APIRouter(prefix="/api/blogs", tags=["Blogs"])


def routing(router: APIRouter):

    @router.get("/")
    def get_blogs():
        return ["b", "b", "c"]

    return None


routing(blogs_router)
