import datetime


from sqlalchemy import (Table, Column, Integer, String, MetaData, TIMESTAMP, ForeignKey, Boolean, Float, DateTime, Text,
                        LargeBinary, JSON)
from sqlalchemy.orm import relationship

from src.database import Base

metadata = MetaData()


class Users(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    phone = Column(String)
    is_active = Column(Boolean, default=True)

    user_in_pereval = relationship("PerevalAdded", back_populates="pereval_in_user")


class Coords(Base):

    __tablename__ = 'coords'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Integer)


class Status(Base):

    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    permissions = Column(JSON)


class PerevalAdded(Base):

    __tablename__ = "pereval_added"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    add_time = Column(DateTime)
    title = Column(String)
    other_titles = Column(String)
    beauty_title = Column(String)
    content = Column(Text)
    level_winter = Column(Text)
    level_summer = Column(Text)
    level_autumn = Column(Text)
    level_spring = Column(Text)
    date_added = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    coords = Column(Integer, ForeignKey("coords.id"))
    status = Column(Integer, ForeignKey("status.id"), default=1)
    connect = Column(Boolean, default=False, nullable=False)

    pereval_in_user = relationship('User', back_populates="user_in_pereval")
    pereval_in_coords = relationship('Coords', back_populates="coords_in_pereval")
    pereval_in_status = relationship('Status', back_populates="status_in_pereval")
    pereval_in_images = relationship('PerevalAddedImages', back_populates="images_in_pereval")


class PerevalAreas(Base):
    __tablename__ = "pereval_areas"
    id = Column(Integer, primary_key=True)
    id_parent = Column(Integer)
    title = Column(String)


class PerevalImages(Base):
    __tablename__ = "pereval_images"
    date_added = Column(TIMESTAMP)
    img = Column(LargeBinary, nullable=True)
    id = Column(Integer, primary_key=True)

    pereval_images_in_images = relationship('PerevalAddedImages', back_populates="images_in_pereval_images")


class PerevalAddedImages(Base):
    __tablename__ = 'pereval_added_images'
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey('pereval_images.id'))
    pereval_id = Column(Integer, ForeignKey('pereval_added.id'))

    images_in_pereval_images = relationship('PerevalImages', back_populates="pereval_images_in_images")
    images_in_pereval = relationship('PerevalAdded', back_populates="pereval_in_images")


class SprActivitiesType(Base):
    __tablename__ = 'spr_activities_type'
    id = Column(Integer, primary_key=True)
    title = Column(String)