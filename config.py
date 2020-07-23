import os

class Config:
    '''
    class that defines app configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Reciped!'
    SENDER_EMAIL = 'testme3848@gmail.com'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tom:psql3848@localhost/blogs'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
