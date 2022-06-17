from project.dao.models.base import BaseMixin
from project.setup_db import db
from project.dao.models.genre import GenreModel
from project.dao.models.director import DirectorModel


class MovieModel(BaseMixin, db.Model):
    __tablename__ = "movie"
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)

    genre = db.relationship("GenreModel")
    director = db.relationship("DirectorModel")

    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"
