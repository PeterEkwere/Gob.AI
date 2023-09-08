#!/usr/bin/python3
"""
    This is the Comment Class
    Author: Peter Ekwere
"""
from models.base_model import BaseModel

class Comment(BaseModel):
    """ This class would handle comments/review 
    """
    recipe_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)