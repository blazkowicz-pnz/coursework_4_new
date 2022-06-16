from project.dao.genre import GenreDAO
from project.schemas.genre import GenreSchema
class GenresService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_item_by_id(self, g_id):
        genre = self.genre_dao.get_by_id(g_id)
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = self.genre_dao.get_all()
        return GenreSchema(many=True).dump(genres)