#!/usr/bin/python3
""" Database class """

from models.base_model import Base
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStore:
    """ Storage class to interact with Mysql database """

    __engine = None
    __session = None

    def __init__(self):
        """ instantiates the storage object """

        DB_USER = os.getenv('DB_USER')
        DB_PWD = os.getenv('DB_PWD')
        DB_HOST = os.getenv('DB_HOST')
        DB_NAME = os.getenv('DB_NAME')
        DB_ENV = os.getenv('DB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{DB_USER}:{DB_PWD}\
                                       @{DB_HOST}/{DB_NAME}')

#    if DB_ENV == 'test':
#        Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """ Adds a new object to the database """
        self.session.add(obj)

    def save(self):
        """ saves an object to the database """
        self.__session.commit()

    def reload(self):
        """ Reloads database """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ calls remove method on the session attribute """
        self.session.remove()
