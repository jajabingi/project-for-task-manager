from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from pydantic import model_validator

class TaskCreate(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=255
    )

    description: str | None = None


class TaskUpdate(BaseModel):

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    description: str | None = None

    completed: bool | None = None


    @model_validator(mode="after")
    def validate_title(self):

        if "title" in self.model_fields_set and self.title is None:
            raise ValueError("Title cannot be null")

        return self


class TaskResponse(BaseModel):

    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )