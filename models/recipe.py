#!/usr/bin/python
"""
    This Module contains the Recipe class
    Author: Peter Ekwere
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_type == 'db':
    recipe_ingredients = Table('recipe_ingredients', Base.metadata,
                          Column('recipe_id', String(60),
                                 ForeignKey('recipe.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('ingredient_id', String(60),
                                 ForeignKey('ingredient.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Recipe(BaseModel, Base):
    """Representation of a Recipe """
    if models.storage_type == 'db':
        __tablename__ = 'recipe'
        ingredient_id = Column(String(60), ForeignKey('ingredient.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        ingredients = relationship("Ingredient",
                               backref="place",
                               cascade="all, delete, delete-orphan",
                               single_parent=True)
    else:
        user_id = ""
        name = ""
        description = ""
        ingredient_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if models.storage_type != 'db':
        @property
        def ingredients(self):
            """getter attribute returns the list of ingredient instances"""
            return self.ingredients
        
    def process_recipe_data(recipe_data):
        """ This method takes a spooncular recipe data ane processes it

        Args:
            recipe_data (str): This is a json response
        """
        response_data = {
            'recipe': recipe_data[0]['name'],
            'instructions': []
        }
        
        #Extract instructions
        for instruction_step in recipe_data[0]['steps']:
            response_data['instructions'].append(instruction_step['step'])
            
        return response_data