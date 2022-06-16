from project.dao import MovieDAO
from project.schemas.movie import MovieSchema


class MoviesService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_item_by_id(self, m_id: int):
        movie = self.movie_dao.get_by_id(m_id)
        return MovieSchema().dump(movie)

    def get_all_movies(self):
        movies = self.movie_dao.get_all()
        return MovieSchema(many=True).dump(movies)
