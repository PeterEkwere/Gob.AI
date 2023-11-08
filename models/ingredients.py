#!/usr/bin/python
"""
    This Module contains the Ingredient class
    Author: Peter Ekwere
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Ingredient(BaseModel, Base):
    """Representation of an Ingredient """
    if models.storage_type == 'db':
        __tablename__ = 'ingredient'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes ingredient"""
        super().__init__(*args, **kwargs)
