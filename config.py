class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///default.db'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/production_db'