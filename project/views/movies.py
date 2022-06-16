from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound
from project.container import movie_service


movies_ns = Namespace("movies")

@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.response(200, "OK")
    def get(self):
        return movie_service.get_all_movies()


@movies_ns.route("/<int:movie_id>/")
class MoviesView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        try:
            return movie_service.get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")

