class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

