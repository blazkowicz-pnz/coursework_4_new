from project.dao.director import DirectorDAO
from project.schemas.director import DirectorSchema


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_item_by_id(self, d_id):
        director = self.director_dao.get_by_id(d_id)
        return DirectorSchema().dump(director)

    def get_all_directors(self):
        directors = self.director_dao.get_all()
        return DirectorSchema(many=True).dump(directors)