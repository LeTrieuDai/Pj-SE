from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "todo_db"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "tasks"
)