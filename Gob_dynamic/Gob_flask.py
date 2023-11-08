#!/usr/bin/python
"""
    This Flask Module Starts a Flash Web Application
    Author: Peter Ekwere
"""
from models import storage
from models.user import User
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/Home/', strict_slashes=False, endpoint='Home')
def hbnb():
    """ Home Route"""
    return render_template('index.html',
                           cache_id=str(uuid.uuid4()))
    
@app.route('/login/', strict_slashes=False, endpoint='login')
def hbnb():
    """ Login Route"""
    return render_template('login.html',
                           cache_id=str(uuid.uuid4()))
    
@app.route('/signup/', strict_slashes=False, endpoint='signup')
def hbnb():
    """ signup Route"""
    return render_template('Signup.html',
                           cache_id=str(uuid.uuid4()))
    
@app.route('/explore/', strict_slashes=False, endpoint='explore')
def hbnb():
    """ Browse Recipes Route"""
    return render_template('explore.html',
                           cache_id=str(uuid.uuid4()))

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
