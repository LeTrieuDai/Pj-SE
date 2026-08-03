from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

client = AsyncIOMotorClient(MONGO_URI)

db = client[DATABASE_NAME]

task_collection = db[COLLECTION_NAME]
