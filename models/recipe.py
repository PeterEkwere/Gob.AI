#!/usr/bin/python3
"""
    This is the Recipe class
    Author: Peter Ekwere
"""
from models.base_model import BaseModel
from uuid import uuid4


class Recipe(BaseModel):
    """Represents a recipe in the system.

    Attributes:
        ingredients (obj): The ingredient.
        Instruction (str): The Recipe instruction        

    Args:
        BaseModel (Class type): This is the parent function that handles global attributes/methods
    """
   
    def __init__(self, name, ingredients, instruction):
        self.id = str(uuid4())
        self.name = name
        self.ingredients = ingredients
        self.instruction = instruction