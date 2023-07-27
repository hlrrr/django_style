from dataclasses    import dataclass

@dataclass()
class Configs:
    DATABASE_HOSTNAME:str = 'mybrain.store'
    DATABASE_PORT:int = 15432
    DATABASE_PASSWORD:str = '1q2w3e4r5t'
    DATABASE_NAMEL:str = 'auth'
    DATABASE_username:str = 'lima'
    DATABASE_URL:str = 'postgresql://lima:1q2w3e4r5t@211.117.18.86:15432/auth'
    DATABASE_URL_alembic:str = 'postgresql+psycopg2://lima:1q2w3e4r5t@211.117.18.86:15432/auth'
    SECRETE_KEY:str = 'some_random_key'
    ALGORITHM:str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 999

