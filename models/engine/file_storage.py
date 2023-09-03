#!/usr/bin/python3
"""
    This is the File_storage class
    Author: Peter Ekwere
"""
import sys
import os
from models.base_model import BaseModel
from models.user import User
from uuid import uuid4
sys.path.append("..")
import json

class FileStorage:
    """ This is the Class that will handle:
                json serialization and deserialization of Data
                and also storing of objects to file
    """
    __PATH: str = "./file.json"
    __objects: dict = {}
    
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
        with open(self.__PATH, mode="w", encoding="utf-8") as a:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            print(new_dict)
            json.dump(new_dict, a)
            
    def reload(self):
        """ This function deserializes an object from a json file
        """
        try:
            if os.path.exists(FileStorage.__PATH):
                with open(FileStorage.__PATH, mode="r", encoding="utf-8") as e:
                    serialized_dict = json.load(e)
                    for key, values in serialized_dict.items():
                        class_name = values["__class__"]
                        an_object = eval(class_name)(**values)
                        self.__objects[key] = an_object
        except FileNotFoundError:
            pass