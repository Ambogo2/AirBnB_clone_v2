#!/usr/bin/python3
"""This module defines a class to manage DBStorage for hbnb clone"""

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from models.base_model import Base
from sqlalchemy import create_engine
import os
from os import sys
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage():
    """Database Storage"""

    __engine = None
    __session = None

    def __init__(self):
        """initialises values and links to the database"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(sys.argv[1],
                                              sys.argv[2], sys.argv[3]),
                                      pool_pre_ping=True)

        if env == "test":
            Base.meta.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session,return a dictionary
        Args:
            cls (class): Optional. Class name of the objects to query.
        Returns:
            dict: A dictionary of objects queried from the session.
        """

        classes = (Amenity, City, Place, Review, State, User)
        objects = dict()

        if cls is None:
            for item in classes:
                query_result = self.__session.query(item)
                for obj in query_result.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj

        else:
            query_result = self.__session.query(cls)
            for obj in query_result.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        my_session = scoped_session(Session)
        self.__session = my_session()

    def close(self):
        """Close the query"""
        self.__session.close()
