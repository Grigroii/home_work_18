class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug =True
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
