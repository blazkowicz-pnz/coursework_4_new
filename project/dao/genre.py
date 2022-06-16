from project.dao.models import GenreModel


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        return self.session.query(GenreModel).filter(GenreModel.id == pk).one_or_none()

    def get_all(self):
        return self.session.query(GenreModel).all()
