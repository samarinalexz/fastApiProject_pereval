import datetime

from sqlalchemy import (Table, Column, Integer, String, MetaData, TIMESTAMP, ForeignKey, Boolean, Float, DateTime, Text,
                        LargeBinary)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
   Column("id", Integer, primary_key=True),
    Column("email", String(40), unique=True, index=True, nullable=False),
    Column("name", String(100), nullable=False),
    Column("password", String(), nullable=False),
    Column("phone", String(100)),
    Column(
        "is_active",
        Boolean(),
        nullable=False,
    ),
)


coords = Table(
    'coords',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("height", Integer),
)


pereval_added = Table(
    "pereval_added",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey(users_table.c.id)),
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
    Column(
        "connect",
        Boolean(),
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