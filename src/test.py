
from prisma_init import prisma_client
import asyncio


async def main():
    await prisma_client.connect()
    await prisma_client.disconnect()
    return None


asyncio.run(main())