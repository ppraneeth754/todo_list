
class Config:
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    # secret key for test created by secret lib ib python
    SECRET_KEY='secrets'


class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False
