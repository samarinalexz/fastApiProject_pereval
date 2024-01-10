from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    phone: str


class UserCreate(UserBase):
    email: str
    username: str
    phone: str


class User(UserBase):
    id: int
    user_in_pereval_id: int
    email: str
    username: str
    phone: str

    class Config:
        orm_mode = True



class PerevalBase(BaseModel):
    email: str
    username: str
    phone: str
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


class PerevalCreate(PerevalBase):
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


class Pereval(PerevalBase):
    id: int
    user: list[User] = []
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

    class Config:
        orm_mode = True


class PerevalUpdate(PerevalBase):
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


