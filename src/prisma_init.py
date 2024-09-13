# coding:utf-8
from fastapi import FastAPI
from prisma import Prisma
from contextlib import asynccontextmanager

prisma_client = Prisma(auto_register=True)


@asynccontextmanager
async def api_lifespan(app: FastAPI):
    await prisma_client.connect()
    yield
    await prisma_client.disconnect()
