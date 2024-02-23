#!/user/bin/python3
""" Seller class """

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String

class Seller(BaseModel, Base):
    """ Seller table in DB """

    __tablename__ = 'sellers'
    username = Column(String(60))
    first_name = Column(String(60))
    last_name = Column(String(60))
    contact = Column(String(60))
    location = Column(String(60))
