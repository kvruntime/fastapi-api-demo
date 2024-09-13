# coding:utf-8

from dtos import PostCreateDto, PostUpdateDto
import prisma_init
from prisma.models import Post


class PostUseCase:
    def __init__(self) -> None:
        self.client = prisma_init.prisma_client
        return

    async def get_all_post(self):
        return await self.client.post.find_many()

    async def get_post_by_id(self, id: str):
        return await self.client.post.find_unique(where={"id": id})

    async def create_new_post(self, dto: PostCreateDto):
        post = await self.client.post.create(
            data={"content": dto.content, "title": dto.title}
        )
        return post

    async def delete_post_by_id(self, id: str):
        # post = await self.client.post.delete(where={"id": id})
        post = await Post.prisma().delete(where={"id": id})
        return post

    async def update_post(self, id: str, dto: PostUpdateDto):
        post = await Post.prisma().update(
            data=dto.model_dump(exclude_defaults=True), where={"id": id}
        )
        return post
