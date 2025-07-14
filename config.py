import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'

    # -----------------------------------------------
    # LOCAL DEVELOPMENT (default) – using SQLite
    # -----------------------------------------------
    '''
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "app.db")}'
    '''
    # -----------------------------------------------
    #  PRODUCTION / DOCKER / K8S – MySQL settings
    # (will be activated later by uncommenting below)
    # -----------------------------------------------

    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_NAME = os.environ.get('DB_NAME', 'flask_mvc_db')

    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


    SQLALCHEMY_TRACK_MODIFICATIONS = False
