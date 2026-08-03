from app.database import task_collection
from bson import ObjectId


async def get_all_tasks():

    tasks = []

    async for task in task_collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)

    return tasks


async def create_task(task):

    result = await task_collection.insert_one(task.model_dump())

    return {
        "message": "Task created",
        "id": str(result.inserted_id)
    }
    
    
async def get_task_by_id(task_id: str):

    task = await task_collection.find_one(
        {"_id": ObjectId(task_id)}
    )

    if task is None:
        return None

    task["_id"] = str(task["_id"])

    return task

async def update_task(task_id: str, task):

    result = await task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {
            "$set": task.model_dump()
        }
    )
    return result.modified_count

async def delete_task(task_id: str):

    result = await task_collection.delete_one(
        {"_id": ObjectId(task_id)}
    )

    return result.deleted_count