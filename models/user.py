#!/usr/bin/python
"""
    This Module contains the User class
    Author: Peter Ekwere
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        user_name = Column(String(128), nullable=True)
        recipes = relationship("Recipe", backref="user")
    else:
        email = ""
        password = ""
        user_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = bcrypt.generate_password_hash(value).decode('utf-8')

        super().__setattr__(name, value)

    def check_password(self, password):
        """ This method checks if password matches stored hash

        Args:
            password (str): This is the users gotten password
        """
        try:
            return bcrypt.check_password_hash(self.password, password)
        except Exception as e:
            print(f"Error checking password: {e}")
            return False