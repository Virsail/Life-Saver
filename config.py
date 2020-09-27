import os



class Config:
    '''
    general configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://virsail:sophy@localhost/syco'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT  =  587
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
    SECRET_KEY = os.environ.get('SECRET_KEY')


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}