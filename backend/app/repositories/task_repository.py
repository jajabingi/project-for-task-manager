from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def get_all(db: Session, skip: int = 0, limit: int = 100):

    statement = (
        select(Task)
        .order_by(Task.id)
        .offset(skip)
        .limit(limit)
    )

    return db.scalars(statement).all()


def get_by_id(db: Session, task_id: int):

    return db.get(Task, task_id)


def create(db: Session, task_data: TaskCreate):

    task = Task(**task_data.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def update(db: Session, task: Task, task_data: TaskUpdate):

    update_data = task_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


def delete(db: Session, task: Task):

    db.delete(task)
    db.commit()