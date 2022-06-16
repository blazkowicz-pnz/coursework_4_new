from project.dao.models.user import UserModel
from project.schemas.user import UserSchema

class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_user_by_id(self, uid: int):
        user = self.session.query(UserModel).filter(UserModel.id == uid).one_or_none()
        return UserSchema().dump(user)

    def update(self):
        ...

