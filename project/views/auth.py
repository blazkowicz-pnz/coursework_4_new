from project.container import auth_service
from flask_restx import Resource, Namespace
from flask import request, redirect


auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class RegisterView(Resource):
     def post(self):
        data = request.json
        auth_service.register(
            email= data["email"],
            password=data["password"]
        )
        return redirect("/")


@auth_ns.route("/login/")
class LoginView(Resource):
    def post(self):
        data = request.json
        tokens = auth_service.login(
            email=data["email"],
            password=data["password"]
        )
        return tokens, 200

    def put(self):
        refresh_token = request.json["refresh_token"]
        return auth_service.update_tokens(refresh_token)
