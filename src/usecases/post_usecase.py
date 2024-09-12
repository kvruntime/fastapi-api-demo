# coding:utf-8

import prisma_init


class PostUseCase:
    def __init__(self) -> None:
        self.client = prisma_init.prisma_client
        return
    async def get_all_post(self):
        return await self.client.post.find_many()