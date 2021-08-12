import os
from flask import (
  Flask,
  render_template,
  request,
  abort
  )
from sqlalchemy import exc
import json
from flask_cors import CORS
from .src.auth.auth import perok

from flask_migrate import Migrate
from .src.database.models import (
  db,
  db_drop_and_create_all,
  setup_db,
  Movie,
  Cartoon
  )


# M y # f i f t h # # #
 # # # # # # # # # # #
  # p r o j e c t ! #
   # # # # # # # # #
    # c a p - # # #
     # s t o n e #
      # # # # ! #
       # # # # #
        # # # #
         # # #
          # #
           #



app = Flask(__name__, template_folder='../frontend/src')


def create_app(app=app):

  setup_db(app)
  CORS(app)

  migrate = Migrate(app, db)
  # can remove this
  # db_drop_and_create_all()

  @app.route('/')
  def index():
    return render_template('layouts/main.html')

  @app.route('/get-movies', methods=['GET'])
  @perok('get:get-movies')
  def local_get_movies_details(payload):
    movies = Movie.query.all()
    return render_template('pages/movies_details.html', data=movies, name="MOVIES DETAILS")

  @app.route('/movies')
  def local_get_movies():
    movies = Movie.query.all()
    return render_template('pages/movies.html', data=movies, name="ALL MOVIES")



  @app.route('/get-cartoons', methods=['GET'])
  @perok('get:get-cartoons')
  def local_get_cartoons_details(payload):
    cartoons = Cartoon.query.all()
    return render_template('pages/movies_details.html', data=cartoons, name="CARTOONS DETAILS")

  @app.route('/cartoons')
  def local_get_cartoons():
    cartoons = Cartoon.query.all()
    return render_template('pages/movies.html', data=cartoons, name="ALL CARTOONS")


  @app.route('/docs/api')
  def local_api_docs():
    return render_template('layouts/docs.html')


  @app.errorhandler(404)
  def not_found_page(error):
    return render_template('errors/404.html')
  
  return app

# create_app()




