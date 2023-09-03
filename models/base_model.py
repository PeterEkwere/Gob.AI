#!/usr/bin/python3
"""
    This is the BaseModel that would define all common methods and attribute for other classes
    Author: Peter Ekwere
"""
from uuid import uuid4
from datetime import datetime
import models
import sys
sys.path.append("..")

class BaseModel:
    """Defines all common methods and attributes
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    val = datetime.fromisoformat(value)
                    self.__dict__[key] = value
                if kwargs.get("id", None) is None:
                    self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self) -> str:
        """ The string method

        Returns:
            str: A String Representation
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ This is the Save method
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()
        
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        of the instance """
        obj = {}
        
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                obj[key] = value.isoformat()
            else:
                obj[key] = value
        obj['__class__'] = self.__class__.__name__
        
        return obj
        
                        
    





