# Gob AI - Recipe Generator
This segment of the GobAI project is the version 0.1 with more versions coming soon, this project has collectively covered all the fundamental concepts of higher level programming, OOP, Databases, API, frontend web design, CI/CD Deployment, unittesting.

#### Functionalities of GobAI:
* Generate recipes from input ingredients
* Signup and Login capabilities
* Create Recipe capabilities (To be implemented in later verions)
* Post Recipe capabilitities (To be implemented in later versions)
* Browse Recipe posted by Others
* Create Meal/Diet plan (To be implemented in later versions)
* A Dashboard to monitor all created and posted recipes

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Bug] (#bugs)
* [Usage](#usage)
* [Authors](#authors)
* [License](#license)

## environment
This project is interpreted/tested on Windows using python3 (version 3.4.3) but can be implemented on alternate env


## installation
* Clone this repository: `git clone "https://github.com/peterekwere/GobAI.git"`
* Access GobAI directory: `cd GobAI`

## file-Descriptions
#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance


Classes inherited from Base Model:
* [ingredients.py](/models/ingredients.py)
* [recipe.py](/models/recipe.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage/Database storage class that handles JSON serialization and deserialization or Database Querying and storage :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects
* `def delete(self)` - delete obj from __objects if it’s inside
* `def close(self)` - call reload() method for deserializing the JSON file to objects
* `def get(self)` - Returns the object based on the class name and its ID, or None if not found
* `def count(self)` - count the number of objects in storage

#### [db_storage.py](/models/engine/db_storage.py) - serializes instances to the mysql database & deserializes back to instances
* `def all(self)` - query on the current database session
* `def new(self, obj)` - add the object to the current database session
* `def save(self)` - commit all changes of the current database session
* ` def delete(self)` -  delete from the current database session obj if not None
* `def reload(self)` - reloads data from the database
* `def close(self)` -  call remove() method on the private session attribute
* `def get(self)` - Returns the object based on the class name and its ID, or None if not found
* `def count(self)` -  count the number of objects in storage



#### `/tests` directory contains some unit test cases for this project the rest will come later:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

## bugs
* issue with loggin in when using filestorage in environment (will check that soon for now use DB method)


## usage
in-order to use this web app make sure you have the following softwares installed

#### install the following
    install SQLAlchemy version 2.0.22
    install jinja2 version 3.1.2
    install Flask version 3.0.0
    install Flask-Bcrypt version 1.0.1
    install Flask-Cors version 4.0.0
    install flasgger version 0.9.7.1
#### After installing, follow the steps below to Run
* [Step 0] create the db - Now your mysql must be running so make sure to start it
    `cat gobai_mysql_setup.sql | mysql -uroot -p` 

* [Step 1] launch the Api
    `GOBAI_MYSQL_USER=root GOBAI_MYSQL_PWD=root GOBAI_MYSQL_HOST=localhost GOBAI_MYSQL_DB=gobai_db   GOBAI_TYPE_STORAGE=db GOBAI_API_HOST=0.0.0.0 GOBAI_API_PORT=5001 python -m api.v1.app`

* [Step 2] launch flask server
    `GOBAI_MYSQL_USER=root GOBAI_MYSQL_PWD=root GOBAI_MYSQL_HOST=localhost GOBAI_MYSQL_DB=gobai_db GOBAI_TYPE_STORAGE=db python -m Gob_dynamic.Gob_flask GOBAI_MYSQL_USER=peter GOBAI_MYSQL_PWD=Peter201$ GOBAI_MYSQL_HOST=localhost GOBAI_MYSQL_DB=gobai_db GOBAI_TYPE_STORAGE=db python -m Gob_dynamic.Gob_flask`

* [Step 3] Open Your WebBrowser and type `http://127.0.0.1:5000/Home/` and vuala you can now access GobAI🥳
* ![GObAI](https://github.com/PeterEkwere/Gob.AI/blob/master/Gob_dynamic/static/img/dsd.PNG)
    And if you cant access the website No need to worry, you can check  #bugs if your issue and solution is there if not you can open an issue



## Authors
Peter Ekwere - [Github](https://github.com/peterekwere) / [Gmail] peterekwere007@gmail.com  

## License
Public Domain. No copy write protection. 

