# Televector Capstone Project 

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
psql postgres
CREATE DATABASE televector;
```

### Running the server

1. Run Front App:
```bash
cd backend
export FLASK_APP=app.py
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run --reload
```
2. Run Televector API:
```bash
cd backend/src
export FLASK_APP=api.py
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### To Read Televector API Documentation open in Browser this file `frontend/src/layouts/docs.html`

