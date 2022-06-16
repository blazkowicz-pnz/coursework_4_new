from project.dao.user import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_item_by_id(self, uid):
        user = self.user_dao.get_user_by_id(uid)
        return user

    def update(self):
        ...

    def partial_update(self):
        ...