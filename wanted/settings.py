class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='you-will-never-guess'
    DB_USERNAME='root'
    DB_PASSWORD='wanted'
    DB_HOST='host.docker.internal'
    DATABASE_NAME='wanteddb'
    MYSQL_ROOT_PASSWORD='rootpass'
    DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

class DockerConfig(Config):
    DEBUG = False
    TESTING = False

class LocalConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
