import uuid

from dataclasses import dataclass

from typing import Optional

from datetime import datetime

from pydantic import BaseModel, field_validator, Field, EmailStr


class BlogBase(BaseModel):
    title: str = Field(default=None, max_length=250)
    description: bool = Field(default=False)
    active: bool


class BlogRead(BlogBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class BlogCreate(BlogBase):
    owner_id: uuid.UUID


class BlogUpdate(BlogBase):
    pass
