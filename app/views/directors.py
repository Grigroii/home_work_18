from flask_restx import Resource, Namespace
from flask import request

from app.container import director_dao

from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
@director_ns.param('director_id')
@director_ns.param('genres_id')
@director_ns.param('year')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_dao.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_dao.create(req_json)

        return '', 201


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did):
        director = director_dao.get_one(did)
        return director_schema.dump(director), 200

    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_dao.update(req_json)

        return "", 204

    def patch(self, did):
        req_json = request.json
        req_json["id"] = did

        director_dao.update_partial(req_json)

        return "", 204

    def delete(self, did):
        director_dao.delete(did)


        return "", 204
