from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def get_movie_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie_by_many_filters(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create(self, data):

        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie


    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie



    def delete(self, mid):
        self.session.query(Movie).filter(Movie.id == mid).delete()
        self.session.commit()
