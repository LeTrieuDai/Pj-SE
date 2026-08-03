
from bson import ObjectId
from app.database import get_collection


async def get_all_tasks():
    collection = get_collection()

    tasks = []

    async for task in collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)

    return tasks


async def create_task(task):
    collection = get_collection()

    result = await collection.insert_one(
        task.model_dump()
    )

    return {
        "message": "Task created",
        "id": str(result.inserted_id)
    }


async def get_task_by_id(task_id: str):
    collection = get_collection()

    task = await collection.find_one(
        {"_id": ObjectId(task_id)}
    )

    if task is None:
        return None

    task["_id"] = str(task["_id"])
    
    return task


async def update_task(task_id: str, task):
    collection = get_collection()

    result = await collection.update_one(
        {"_id": ObjectId(task_id)},
        {
            "$set": task.model_dump()
        }
    )

    return result.modified_count


async def delete_task(task_id: str):
    collection = get_collection()

    result = await collection.delete_one(
        {"_id": ObjectId(task_id)}
    )

    return result.deleted_count