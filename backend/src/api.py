import os
from flask import (
  Flask,
  request,
  jsonify,
  abort
  )
from sqlalchemy import exc
import json
from flask_cors import CORS
from .database.models import (
  db_drop_and_create_all,
  db,
  setup_db,
  Movie,
  Cartoon
  )
from flask_migrate import Migrate
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)


def create_api(app=app, test_config=None):
  setup_db(app)
  CORS(app)
  migrate = Migrate(app, db)

  db_drop_and_create_all()
  
  @app.route('/api')
  def main():
    return jsonify({
      'working': True
    })
  
  ### FOR MOVIES {
  
  @app.route('/api/movies')
  def movies():
    Movies= Movie.query.all()
    if len(Movies)==0:
      return jsonify({
        'ok': False,
        'error': 404,
        'message': 'No movies yet'
      }), 404
    movies = []
    for movie in Movies:
      movies.append({
        'title': movie.title,
        'year': int(movie.year)
      })
    return jsonify({
      'ok': True,
      'movies': movies
      }), 200
  
  
  @app.route('/api/get-movies', methods=['GET'])
  @requires_auth('get:get-movies')
  def get_movies(payload):
    moov = Movie.query.all()
    if len(moov)==0:
      return jsonify({
        'ok': False,
        'error': 404,
        'message': 'No movies'
      }), 404
    movies = []
    for movie in moov:
      movies.append({
        'id': movie.id,
        'title': movie.title,
        'year': int(movie.year),
        'director': movie.director,
        'duration': int(movie.duration),
        'country': movie.country,
        'image_link': movie.image_link
      })
    return jsonify({
      'ok': True,
      'movies': movies
      }), 200
  
  @app.route('/api/get-movies/<int:id>', methods=['GET'])
  @requires_auth('get:get-movies')
  def get_movie(payload, id):
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if not movie:
      abort(404)
    movie = {
        'id': movie.id,
        'title': movie.title,
        'year': int(movie.year),
        'director': movie.director,
        'duration': int(movie.duration),
        'country': movie.country,
        'image_link': movie.image_link
    }
    return jsonify({
      'ok': True,
      'movie': movie
      }), 200
  
  @app.route('/api/movies', methods=['POST'])
  @requires_auth('post:movies')
  def new_movie(payload):
    r = request.get_json()
    try:
      title=r['title']
      year=int(r['year'])
      director=r['director']
      duration=int(r['duration'])
      country=r['country']
      link=r['image_link']
      if len(title)==0 or year<=0 or len(director)==0 or duration<=0 or len(country)==0 or len(link)==0:
        abort(422)
      movie = Movie(
          title=title,
          year=year,
          director=director,
          duration=duration,
          country=country,
          image_link=link
      )
      movie.insert()
    except:
      abort(400)
    return jsonify({
      'ok': True,
      'created': {
        'id': movie.id,
        'title': title,
        'year': year,
        'director': director,
        'duration': duration,
        'country': country,
        'image_link': link
      }
    }), 200
  
  @app.route('/api/movies/<int:id>',methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movie(payload, id):
    r = request.get_json() or {}
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if not movie:
      abort(404)
    try:
      changes = {}
      
      title = r.get('title', None)
      year = r.get('year', None)
      director = r.get('director', None)
      duration = r.get('duration', None)
      country = r.get('country', None)
      image_link = r.get('image_link', None)
      
      if title:
        movie.title = title
        changes['title'] = title
      if year:
        movie.year = year
        changes['year'] = year
      if director:
        movie.director = director
        changes['director'] = title
      if duration:
        movie.duration = duration
        changes['duration'] = duration
      if country:
        movie.country = country
        changes['country'] = country
      if image_link:
        movie.image_link = image_link
        changes['image_link'] = image_link
      
      movie.update()
      
    except:
      abort(400)
    return jsonify({
      'ok': True,
      'changes': changes
    }), 200
  
  @app.route('/api/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def del_movie(payload, id):
    r = request.get_json() or {}
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if not movie:
      abort(404)
    try:
      movie.delete()
    except:
      abort(400)
    if r['test']==True:
      db_drop_and_create_all()
    return jsonify({
      'ok': True,
      'delete': id
    }), 200
  
  ### END MOVIES }
  
  


  ### FOR CARTOONS {
  
  @app.route('/api/cartoons')
  def cartoons():
    Cartoons= Cartoon.query.all()
    if len(Cartoons)==0:
      return jsonify({
        'ok': False,
        'error': 404,
        'message': 'No cartoons yet'
      }), 404
    cartoons = []
    for cartoon in Cartoons:
      cartoons.append({
        'title': cartoon.title,
        'year': int(cartoon.year)
      })
    return jsonify({
      'ok': True,
      'cartoons': cartoons
      }), 200
  
  
  @app.route('/api/get-cartoons', methods=['GET'])
  @requires_auth('get:get-cartoons')
  def get_cartoons(payload):
    moov = Cartoon.query.all()
    if len(moov)==0:
      return jsonify({
        'ok': False,
        'error': 404,
        'message': 'No cartoons'
      }), 404
    cartoons = []
    for cartoon in moov:
      cartoons.append({
        'id': cartoon.id,
        'title': cartoon.title,
        'year': int(cartoon.year),
        'director': cartoon.director,
        'duration': int(cartoon.duration),
        'country': cartoon.country,
        'image_link': cartoon.image_link
      })
    return jsonify({
      'ok': True,
      'cartoons': cartoons
      }), 200
  
  @app.route('/api/get-cartoons/<int:id>', methods=['GET'])
  @requires_auth('get:get-cartoons')
  def get_cartoon(payload, id):
    cartoon = Cartoon.query.filter(Cartoon.id==id).one_or_none()
    if not cartoon:
      abort(404)
    cartoon = {
        'id': cartoon.id,
        'title': cartoon.title,
        'year': int(cartoon.year),
        'director': cartoon.director,
        'duration': int(cartoon.duration),
        'country': cartoon.country,
        'image_link': cartoon.image_link
    }
    return jsonify({
      'ok': True,
      'cartoon': cartoon
      }), 200
  
  @app.route('/api/cartoons', methods=['POST'])
  @requires_auth('post:cartoons')
  def new_cartoon(payload):
    r = request.get_json()
    try:
      title=r['title']
      year=int(r['year'])
      director=r['director']
      duration=int(r['duration'])
      country=r['country']
      link=r['image_link']
      if len(title)==0 or year<=0 or len(director)==0 or duration<=0 or len(country)==0 or len(link)==0:
        abort(422)
      cartoon = Cartoon(
          title=title,
          year=year,
          director=director,
          duration=duration,
          country=country,
          image_link=link
      )
      cartoon.insert()
    except:
      abort(400)
    return jsonify({
      'ok': True,
      'created': {
        'id': cartoon.id,
        'title': title,
        'year': year,
        'director': director,
        'duration': duration,
        'country': country,
        'image_link': link
      }
    }), 200
  
  @app.route('/api/cartoons/<int:id>',methods=['PATCH'])
  @requires_auth('patch:cartoons')
  def edit_cartoon(payload, id):
    r = request.get_json() or {}
    cartoon = Cartoon.query.filter(Cartoon.id==id).one_or_none()
    if not cartoon:
      abort(404)
    try:
      changes = {}
      
      title = r.get('title', None)
      year = r.get('year', None)
      director = r.get('director', None)
      duration = r.get('duration', None)
      country = r.get('country', None)
      image_link = r.get('image_link', None)
      
      if title:
        cartoon.title = title
        changes['title'] = title
      if year:
        cartoon.year = year
        changes['year'] = year
      if director:
        cartoon.director = director
        changes['director'] = title
      if duration:
        cartoon.duration = duration
        changes['duration'] = duration
      if country:
        cartoon.country = country
        changes['country'] = country
      if image_link:
        cartoon.image_link = image_link
        changes['image_link'] = image_link
      
      cartoon.update()
      
    except:
      abort(400)
    return jsonify({
      'ok': True,
      'changes': changes
    }), 200
  
  @app.route('/api/cartoons/<int:id>', methods=['DELETE'])
  @requires_auth('delete:cartoons')
  def del_cartoon(payload, id):
    r = request.get_json() or {}
    cartoon = Cartoon.query.filter(Cartoon.id==id).one_or_none()
    if not cartoon:
      abort(404)
    try:
      cartoon.delete()
    except:
      abort(400)
    if r['test']==True:
      db_drop_and_create_all()
    return jsonify({
      'ok': True,
      'delete': id
    }), 200
  
  ### END MOVIES }


  
  
  ### ERROR HANDLING {
  
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "ok": False,
          "error": 422,
          "message": "Unprocessable"
      }), 422
  
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "ok": False,
        "error": 404,
        "message": "Not Found"
        }), 404
  
  @app.errorhandler(405)
  def unprocessable(error):
      return jsonify({
          "ok": False,
          "error": 405,
          "message": "Method Not Allowed"
      }), 405
  
  @app.errorhandler(AuthError)
  def auth_errors(error):
      return jsonify({
          "ok": False,
          "error": error.status_code,
          "message": error.error['description']
      }), error.status_code
  
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "ok": False,
          "error": 400,
          "message": 'Bad Request'
      }), 400
  
  ### ERROR HANDLERS }
  
  
  
  return app

create_api()

# end .