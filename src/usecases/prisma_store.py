# coding:utf-8

import typing
import prisma_init
from usecases.repository import IPostRepo
from prisma.models import Post


class PrismaPostRepo(IPostRepo):
    def __init__(self) -> None:
        super().__init__()
        self.client = prisma_init.prisma_client
        return

    async def get_all(self) -> typing.List[Post]:
        posts = await self.client.post.find_many()
        return posts
