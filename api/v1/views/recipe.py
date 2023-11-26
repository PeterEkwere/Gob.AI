#!/usr/bin/python
"""
    The Following Objects Handle all RestFul API actions for User login
    Author: Peter Ekwere
"""
from models.recipe import Recipe
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json
import requests
import random

def get_recipe_from_spoocular(ingredients):
    """ This Method takes a list of ingredients and returns a recipe

    Returns:
        str: a Recipe
        str: the api key
    """
    spooncular_api_key = '7d077305901b477ebba66bbb0c0f846e'
    spoon_headers = {'X-Api-Key': spooncular_api_key}
    spooncular_url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number={1}'
    Recipe_response = requests.get(spooncular_url, headers=spoon_headers).json()
    
    return Recipe_response


def get_recipe_instruct_from_spooncular(recipe_name, recipe_id):
    """ This function takes a recipe name and checks for instructions in the spoocular api

    Args:
        recipe_name (str): This is the recipe name
    """
    spooncular_api_key = '7d077305901b477ebba66bbb0c0f846e'
    spoon_headers = {'X-Api-Key': spooncular_api_key}
    instruction_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    instruction_Response = requests.get(instruction_url, headers=spoon_headers).json()
    recipe = Recipe.process_recipe_data(instruction_Response)
    recipe['recipe'] = recipe_name
    
    return instruction_Response

def get_recipe_instruct_from_ninja(recipe_name):
    """ This function takes a recipe name and checks for instructions on how to prepare from the api ninja

    Args:
        recipe_name (str): this is the recipe name

    Returns:
        dict : instructions for a recipe
    """
    ninjaApiKey = {'X-Api-Key': 'WIJDf8xbrfKN8JSUcgMG7w==tyiMmsqjzJOlKJdg'}
    api_url = f'https://api.api-ninjas.com/v1/recipe?query={recipe_name}'
    response = requests.get(api_url, headers=ninjaApiKey)
    
    if not response.text or response.text is None or response.text == "[]":
        return None
    return response.text


@app_views.route('/recipe', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/recipe.yml', methods=['POST'])
def get_recipe():
    """
    gets a recipe from a list of ingredients
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'ingredients' not in request.get_json():
        abort(400, description="ingredients missing")
    
    data = request.get_json()
    ingredients = data.get('ingredients')
    
    Recipe_response = get_recipe_from_spoocular(ingredients)
    recipe_id = Recipe_response[0]['id']
    recipe_name = Recipe_response[0]['title']
    
    tokenized_recipe = recipe_name.split()
    
    try_recipe = get_recipe_instruct_from_ninja(recipe_name)
       
    
    if try_recipe is None :
        for token in tokenized_recipe:
            a_recipe = get_recipe_instruct_from_ninja(token)
            if a_recipe is None:
                break
            else:
                return json.dumps(a_recipe), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps(try_recipe), 200, {'ContentType': 'application/json'}
    
    if a_recipe is None:
        spoon_recipe = get_recipe_instruct_from_spooncular(recipe_name, recipe_id)
        if spoon_recipe:
            return json.dumps(spoon_recipe), 200, {'ContentType': 'application/json'}    
    
   
    return jsonify({"message": "Invalid Recipe"}), 401
    