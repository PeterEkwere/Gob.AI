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


@app_views.route('/recipe', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/recipe.yml', methods=['GET'])
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
    
    spooncular_api_key = '7d077305901b477ebba66bbb0c0f846e'
    spoon_headers = {'X-Api-Key': spooncular_api_key}
    spooncular_url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number={1}'
    Recipe_response = requests.get(spooncular_url, headers=spoon_headers).json()
    recipe_id = Recipe_response[0]['id']
    recipe_name = Recipe_response[0]['title']
    instruction_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    instruction_Response = requests.get(instruction_url, headers=spoon_headers).json()
    recipe = Recipe.process_recipe_data(instruction_Response)
    recipe['name'] = recipe_name
    if recipe:
        return json.dumps(recipe), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({"message": "Invalid Recipe"}), 401
    