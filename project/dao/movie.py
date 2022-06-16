from project.dao.models import MovieModel



class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, m_id: int):
        return self.session.query(MovieModel).filter(MovieModel.id == m_id).one_or_none()

    def get_all(self):
        return self.session.query(MovieModel).all()
