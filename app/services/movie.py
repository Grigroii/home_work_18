from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self):
        return self.movie_dao.get_movies()

    def get_movie_by(self, id=None, director_id=None, genre_id=None, year=None):
        if director_id is not None:
            return self.movie_dao.get_movie_by_director_id(director_id)
        elif id is not None:
            return self.movie_dao.get_movie_by_id(id)
        elif genre_id is not None:
            return self.movie_dao.get_movie_by_genre_id(genre_id)
        elif year is not None:
            return self.movie_dao.get_movie_by_year(year)
        else:
            return []

    def add_movie(self, data):
        self.movie_dao.create(data)

    def update_movie(self, data):
        mid = data.get("id")

        movie = self.get_movie_by(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.movie_dao.update(movie)

    def delete(self, mid):
        self.movie_dao.delete(mid)
