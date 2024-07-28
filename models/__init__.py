#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



db_storage = getenv("HBNB_TYPE_STORAGE")
if db_storage == "db":
    storage = DBStorage
else:
    storage = FileStorage()

storage.reload()
