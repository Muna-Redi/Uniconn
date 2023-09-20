#!/usr/bin/python3
""" Database class """

from models.base_model import Base
from models.seller import Seller
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker




class DBStore:
    """ Storage class to interact with Mysql database """

    __engine = None
    __session = None

    def __init__(self):
        """ instantiates the storage object """
        DB_USER = getenv('DB_USER')
        DB_PWD = getenv('DB_PWD')
        DB_HOST = getenv('DB_HOST')
        DB_NAME = getenv('DB_NAME')
        DB_ENV = getenv('DB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(DB_USER,
                                             DB_PWD,
                                             DB_HOST,
                                             DB_NAME))
        if DB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """ Adds a new object to the database """
        self.__session.add(obj)

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
