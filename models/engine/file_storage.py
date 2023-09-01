#!/usr/bin/python3
"""
    This is the File_storage class
    Author: Peter Ekwere
"""
import sys
import os
sys.path.append("..")
from models.base_model import BaseModel

class FileStorage:
    """ This is the Class that will handle:
                json serialization and deserialization of Data
                storing of objects to file
    """
    
    PATH = "file.json"
    objects = {}
    
    def all(self):
        """ This Function Returns all objects
        """
        return self.__objects
    
    def new(self, obj):
        """ This function sets a new object in the objects dictionary with its id
        """
        obj_id = f"{obj.__class__.name}.{obj.id}"
        self.__objects[obj_id] = obj
        
    def save(self):
        """ This function serializes an object to a json file
        """
        