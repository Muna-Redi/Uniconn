#!/usr/bin/python3
""" Base Model Class """

import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
import uuid


Base = declarative_base()

class BaseModel:
    """ Base Class """
    id = Column(String(60), primary_key=True)

    def __init__(self):
        """ initializer """

        self.id = str(uuid.uuid4())

    def save(self):
        """ save object in storage """
        models.storage.new(self)
        models.storage.save()
