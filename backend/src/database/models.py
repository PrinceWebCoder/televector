from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
import os
import psycopg2

# DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
# DB_USER = os.getenv('DB_USER', 'postgres')  
# DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')  
# DB_NAME = os.getenv('DB_NAME', 'televector')  
# database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

database_path = 'postgresql://apsuubnjllwwea:2f657562b880a6c452d8f92ee2c2af4e43269ebe2d4993e70b0564c8367be4cc@ec2-18-213-219-169.compute-1.amazonaws.com:5432/d57e6tsvqs3ner'



db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    
    # Example Movies {
    titles = [
      "Titanic",
      "The Tomorrow War",
      "Terminator 2: Judgment Day",
      "Unhinged",
      "Anna"
      ]
    years = [
      1997,
      2021,
      1991,
      2020,
      2019
      ]
    directors = [
      "James Cameron",
      "Chris McKay",
      "James Cameron",
      "Derrick Borte",
      "Luc Besson"
      ]
    durations = [
      195,
      138,
      137,
      93,
      119
      ]
    countries = [
      "USA",
      "USA",
      "USA",
      "USA",
      "France"
      ]
    links = [
      "https://upload.wikimedia.org/wikipedia/en/1/19/Titanic_%28Official_Film_Poster%29.png",
      "https://upload.wikimedia.org/wikipedia/en/6/60/The_Tomorrow_War_%282021_film%29_official_theatrical_poster.jpg",
      "https://www.filmsite.org/posters/terminator2.jpg",
      "https://m.media-amazon.com/images/I/51CDBrqqrbL._AC_SY580_.jpg",
      "https://m.media-amazon.com/images/I/51C0L2jZbjL._AC_SY580_.jpg"
      ]
    l = len(titles)
    for i in range(l):
      movie = Movie(
        title = titles[i],
        year = years[i],
        director = directors[i],
        duration = durations[i],
        country = countries[i],
        image_link = links[i]
      )
      movie.insert()
    # }
    
    # Example Cartoons {
    titles = [
      "Onward",
      "Три богатыря и Шамаханская царица",
      "Zootopia"
      ]
    years = [
      2020,
      2010,
      2016
      ]
    directors = [
      "Dan Scanlon",
      "Сергей Глезин",
      "Byron Howard"
      ]
    durations = [
      102,
      77,
      108
      ]
    countries = [
      "USA",
      "Russia",
      "USA"
      ]
    links = [
      "https://m.media-amazon.com/images/I/91X-d7oq8jL._AC_SL1500_.jpg",
      "https://popkult.org/wp-content/uploads/2016/08/tribogatyra3_poster4.jpg",
      "https://pyxis.nymag.com/v1/imgs/117/650/b3d1f5e3247e0024133a89325cb1e23412-07-zootopia.2x.rsquare.w700.jpg"
      ]
    l = len(titles)
    for i in range(l):
      cartoon = Cartoon(
        title = titles[i],
        year = years[i],
        director = directors[i],
        duration = durations[i],
        country = countries[i],
        image_link = links[i]
      )
      cartoon.insert()
    # }
    



class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(String(128), nullable=False)
    # duration // in minutes
    duration = Column(Integer, nullable=False)
    country = Column(String(128), nullable=False)
    image_link = Column(String(512), nullable=False)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Cartoon(db.Model):
    __tablename__ = 'cartoon'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(String(128), nullable=False)
    # duration // in minutes
    duration = Column(Integer, nullable=False)
    country = Column(String(128), nullable=False)
    image_link = Column(String(512), nullable=False)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()






# end .
