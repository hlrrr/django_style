from dataclasses    import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.abspath(__file__)))

@dataclass
class Config:
    BASE_DIR:str = base_dir
    SECRETE_KEY:str = 'some_random_key'
    ALGORITHM:str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 999
    DEBUG:bool = False
    TRUSTED_HOSTS = ['']
    ALLOW_SITE = ['']

@dataclass
class LocalConfig(Config):
    DATABASE_HOSTNAME:str = 'localhost'
    DATABASE_PORT:int = 13306
    DATABASE_PASSWORD:str = '1q2w3e4r5t'
    DATABASE_NAME:str = 'contacts'
    DATABASE_USERNAME:str = 'lima'
    DATABASE_URL:str = 'mysql+pymysql://lima:1q2w3e4r5t@127.0.0.1:13306/contacts'
    DEBUG:bool = True
    TRUSTED_HOSTS = ['*']
    ALLOW_SITE = ['*']


@dataclass
class ProdConfig(Config):
    pass


@dataclass
class TestConfig(Config):
    pass


def config():
    ''' select environmets  '''
    config = dict(prod=ProdConfig, local=LocalConfig, test=TestConfig)
    return config[environ.get("ENV", "local")]()

