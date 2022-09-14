from flask_restx import Resource, Namespace
from flask import request

from app.container import genre_dao, genre_service

from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200

    def post(self):
        req_json = request.json
        genre_dao.create(req_json)

        return '', 201


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid):

        return genre_schema.dump(genre_service.get_one(gid)), 200

    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_dao.update(req_json)


        return "", 204

    def patch(self, gid):

        req_json = request.json
        req_json["id"] = gid
        genre_dao.update_partial(req_json)

        return "", 204

    def delete(self, gid):

        genre_dao.delete(gid)

        return "", 204
