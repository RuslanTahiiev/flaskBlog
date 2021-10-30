
class Config:

    # Flask
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'overpoweredsecretkey'

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
