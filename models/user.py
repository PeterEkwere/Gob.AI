#!/usr/bin/python3
"""
    This is the User class
    Author: Peter Ekwere
"""
from models.base_model import BaseModel
from uuid import uuid4
class User(BaseModel):
    """Represents a user in the system.

    Attributes:
        first_name (str): The unique username of the user.
        email (str): The email address associated with the user.
        password (str): The Password for the email address
        last_name (str): last name of the user

    Args:
        BaseModel (Class type): This is the parent function that handles global attributes/methods
    """
    email = ""
    password = ""
    first_name = ""
    lase_name = ""
    
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        super().__init__(*args, **kwargs)