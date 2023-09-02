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
                and also storing of objects to file
    """
    
    __PATH = "./file.json"
    __objects = {}
    
    def all(self):
        """ This Function Returns all objects
        """
        return self.__objects
    
    def new(self, obj):
        """ This function sets a new object in the objects dictionary with its id
        """
        obj_id = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_id] = obj
        
    def save(self):
        """ This function serializes an object to a json file
        """
        with open(self.__objects, mode="w", encoding="utf-8") as a:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json_dump(new_dict, a)
            
    def reload(self):
        """ This function deserializes an object from a json file
        """