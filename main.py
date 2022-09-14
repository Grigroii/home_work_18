from flask import Flask
from flask_restx import Api
from app.config import Config

from app.database import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    # create_data(app, db)


#
#
# def create_data(app, db):
# with app.app_context():
# db.create_all()


# with db.session.begin():
# db.session.add_all()
#
#
app = create_app(Config())
app.debug = True
#
if __name__ == '__main__':
    app.run(host="localhost", port=10001)
