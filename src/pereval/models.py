import datetime


from sqlalchemy import (Table, Column, Integer, String, MetaData, TIMESTAMP, ForeignKey, Boolean, Float, DateTime, Text,
                        LargeBinary, JSON)

from src.auth.models import user

metadata = MetaData()

def get_status_list():

    status_list = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    return status_list


def get_new_status():

    return 'New'

coords = Table(
    'coords',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("height", Integer),
)


status = Table(
    'status',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)


pereval_added = Table(
    "pereval_added",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey(user.c.id)),
    Column("add_time", DateTime()),
    Column("title", String(100)),
    Column("other_titles", String(100)),
    Column("beauty_title", String(100)),
    Column("content", Text()),
    Column("level_winter", Text()),
    Column("level_summer", Text()),
    Column("level_autumn", Text()),
    Column("level_spring", Text()),
    Column("date_added", TIMESTAMP, default=datetime.datetime.utcnow),
    Column("coords_id", ForeignKey(coords.c.id)),
    Column('status_id', Integer, ForeignKey(status.c.id), nullable=False),
    Column(
        "connect",
        Boolean(),
        default=False,
        nullable=False,
    ),
)

pereval_areas = Table(
    "pereval_areas",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("id_parent", Integer),
    Column("title", String(100)),

)

pereval_images = Table(
    "pereval_images",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("date_added", TIMESTAMP()),
    Column("img", LargeBinary, nullable=True),

)

pereval_added_images = Table(
    'pereval_added_images',
    metadata,
    Column("image_id", ForeignKey(pereval_images.c.id)),
    Column("pereval_id", ForeignKey(pereval_added.c.id)),

)

spr_activities_type = Table(
    'spr_activities_type',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
)