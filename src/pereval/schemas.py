from datetime import datetime
from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class PerevalCreate(BaseModel):
    id: int
    add_time: datetime
    title: str
    other_titles: str
    beauty_title: str
    content: str
    level_winter: str
    level_summer: str
    level_autumn: str
    level_spring: str
    date_added: datetime
    latitude: float
    longitude: float
    height: int

