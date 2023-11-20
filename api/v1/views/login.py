#!/usr/bin/python
"""
    The Following Objects Handle all RestFul API actions for User login
    Author: Peter Ekwere
"""
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json


@app_views.route('/login', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/login.yml', methods=['POST'])
def login_user():
    """
    logs in a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    
    data = request.get_json()
    password = data.get('password')

    # Get all Users from the database
    users_objects = storage.all(User).values()
    #users_list = []
    user_exist = False
    for user in users_objects:
        if user.check_password(password):
            user_exist = True
            break
    
    if user_exist:
        # User exists and password is correct
        response_data = {
            "user_name": user.user_name,
            "user_id": user.id,
        }
        return json.dumps(response_data), 200, {'ContentType': 'application/json'}
    else:
        # User doesn't exist or password is incorrect
        return jsonify({"message": "Invalid username or password"}), 401
    