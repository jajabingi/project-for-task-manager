from sqlalchemy.orm import Session

from fastapi import HTTPException, status

from app.repositories import task_repository
from app.schemas.task import TaskCreate, TaskUpdate


def get_tasks(db: Session, skip: int = 0, limit: int = 100):

    return task_repository.get_all(db, skip, limit)


def get_task(db: Session, task_id: int):

    task = task_repository.get_by_id(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


def create_task(db: Session, task_data: TaskCreate):

    return task_repository.create(db, task_data)


def update_task(db: Session, task_id: int, task_data: TaskUpdate):

    task = get_task(db, task_id)

    if not task_data.model_fields_set:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No update fields provided"
        )

    return task_repository.update(db, task, task_data)


def delete_task(db: Session, task_id: int):

    task = get_task(db, task_id)

    task_repository.delete(db, task)