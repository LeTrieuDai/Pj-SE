from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DATABASE_NAME

def get_database():
    client = AsyncIOMotorClient(MONGO_URI)
    return client[DATABASE_NAME]

def get_collection():
    return get_database()["tasks"]