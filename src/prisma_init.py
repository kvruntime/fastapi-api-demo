from fastapi import FastAPI
from prisma import Prisma


prisma_client = Prisma(auto_register=True)


def register_prisma(app: FastAPI):
    @app.on_event("startup")
    async def _():
        await prisma_client.connect()

    @app.on_event("shutdown")
    async def _():
        await prisma_client.disconnect()
