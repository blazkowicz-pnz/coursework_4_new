from flask_restx import Resource, Namespace
from project.container import user_service
from flask import request

from project.utils import auth_required, get_id_from_token

user_ns = Namespace("profile")


@user_ns.route("/user/")
class UserView(Resource):
    @auth_required
    def get(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        user_id = get_id_from_token(token)
        user = user_service.get_item_by_id(user_id)
        return user

    def put(self):
        ...

    def patch(self):
        ...

