# Televector App
Simple application for who is interested in watching movies and cartoons! People can create movies and cartoons for spectators. You can get all information about you favourite movies and cartoons before watching them! ENJOY! 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
Run Postgres Database Server and run this command in terminal:
```bash
CREATE DATABASE televector;
```

## Running the server

### Run Front App:
* On Windows:
```bash
cd backend
set FLASK_APP=app.py
set FLASK_DEBUG=true
set FLASK_ENV=development
flask run --reload
```
* On Linux:
```bash
cd backend
export FLASK_APP=app.py
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run --reload
```

### Run Televector API:
* On Windows:
```bash
cd backend/src
set FLASK_APP=api.py
set FLASK_DEBUG=true
set FLASK_ENV=development
flask run --reload
```
* On Linux:
```bash
cd backend/src
export FLASK_APP=api.py
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run --reload
```


The `--reload` flag will detect file changes and restart the server automatically.


### **To Read Televector API Documentation open in Browser this file `/frontend/src/layouts/docs.html` or click "API DOCUMENTATION" button on APP's Heroku Website, and this way is also availible https://televector.herokuapp.com/docs/api**

## APP Resources:
* APP on Heroku: https://televector.herokuapp.com
* APP on GitHub: http://github.com/Esteklo/televector

Fast signup or login: https://mkdir.us.auth0.com/authorize?audience=televector&response_type=token&client_id=2ZGFTZOIJiT0KyrKwmpIULH6rXjNQHIm&redirect_uri=https://televector.herokuapp.com/


### FOR DEVELOPERS
APP test is created with Postman, you can find it from this: `/backend/tests/televector.postman_collection.json` .



