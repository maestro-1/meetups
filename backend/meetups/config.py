import os


Secret_Key = os.environ.get("SECRET_KEY")
Database_Uri = os.environ.get("SQLALCHEMY_DATABASE_URI")


class BaseConfig:
    JWT_SECRET_KEY = Secret_Key
    SQLALCHEMY_DATABASE_URI = Database_Uri
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:admin@127.0.0.1:5432/fashionwares"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:admin@127.0.0.1:5432/fashionwares"
    DEBUG = False
