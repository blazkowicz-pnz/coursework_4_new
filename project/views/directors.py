from project.container import director_service
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound

directors_ns = Namespace("directors")

@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        return director_service.get_all_directors()


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director Not Found")
    def get(self, director_id: int):
        try:
            return director_service.get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")


