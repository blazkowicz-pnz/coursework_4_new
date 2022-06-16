from project.dao.models import DirectorModel

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, d_id):
        return self.session.query(DirectorModel).filter(DirectorModel.id == d_id).one_or_none()

    def get_all(self):
        return self.session.query(DirectorModel).all()
