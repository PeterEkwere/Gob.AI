#!/usr/bin/python3
"""
    This is the Ingredients class
    Author: Peter Ekwere
"""
from uuid import uuid4
class Ingredient():
    """Represents an ingredient in the system.

    Attributes:
        name (str): The name of the ingredient.
        unit (str): The measurements.
        Quantity (str): This is the Quantity of an ingredient needed in a recipe
        

    Args:
        BaseModel (Class type): This is the parent function that handles global attributes/methods
    """
    
    def __init__(self, name=None, Quantity=None, unit=None):
        self.id = str(uuid4())
        self.name = name
        self.Quantity = Quantity
        self.unit = unit