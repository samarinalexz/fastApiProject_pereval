from datetime import datetime

from pydantic import BaseModel


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

