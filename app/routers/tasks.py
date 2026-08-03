from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from app.models import Task
from app.services.task_service import (
    get_all_tasks,
    create_task,
    get_task_by_id,
    update_task,
    delete_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/")
async def get_tasks():
    return await get_all_tasks()

@router.post("/")
async def add_task(task: Task):
    return await create_task(task)

@router.get("/{task_id}")
async def get_task(task_id: str):

    task = await get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@router.put("/{task_id}")
async def edit_task(task_id: str, task: Task):

    updated = await update_task(task_id, task)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task updated"
    }
    
@router.delete("/{task_id}")
async def remove_task(task_id: str):

    deleted = await delete_task(task_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted"
    }