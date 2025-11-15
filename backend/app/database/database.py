from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

from .models import User, Project, Task

DB_URL = str(config("MONGO_URL"))


async def init_db():
    client = AsyncIOMotorClient(DB_URL)
    database = client["projectflowdb"]
    await init_beanie(database=database, document_models=[User, Project, Task])  # type: ignore
