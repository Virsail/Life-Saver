import os
import  you
from dotenv import load_dotenv
load_dotenv()


class Config:
    '''
    general configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://virsail:sophy@localhost/syco'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT  =  465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    



    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    production configuration child class
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}