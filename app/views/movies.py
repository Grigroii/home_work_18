# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace
from flask import request

from app.container import movie_dao
from app.dao.model.movie import MovieSchema
from app.container import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        if director_id := request.args.get("director_id"):
            return movies_schema.dump(movie_service.get_movie_by(director_id=director_id)), 200
        elif genre_id := request.args.get("genre_id"):
            return movies_schema.dump(movie_service.get_movie_by(genre_id=genre_id)), 200
        elif year := request.args.get("year"):
            return movies_schema.dump(movie_service.get_movie_by(year=year)), 200
        else:
            return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        movie_service.add_movie(request.json)

        return '', 201


@movie_ns.route('/<int:mid>')
class MovieViews(Resource):
    def get(self, mid):
        movie = movie_service.get_movie_by(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_service.update_movie(req_json)
        return "", 204


    def delete(self, mid):
        movie_service.delete(mid)

        return "", 204
