#!/usr/bin/python3
""" Buyer model """

from models.base_n=model import Base, BaseModel
from sqlalchemy import Column, String

class buyer(BaseModel, Base):
    """ buyer table in DB """

    __tablename__ = "buyers"
    username = Column(String(60))
    first_name = Column(String(60))
    last_name = Column(String(60))
    email = Column(String(60))
    password = Column(String(60))
    contact = Column(String(60))
    location = Column(String(60))
