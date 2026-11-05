from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.db.database import engine
from app.db.base import Base

# Import models so SQLAlchemy registers their tables.
from app.models.task import Task

from app.api.tasks import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Create tables if they do not exist.
    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="Task Manager REST API",
    version="1.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(tasks_router)


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@app.get("/")
def root():

    return {
        "message": "Task Manager API is running"
    }