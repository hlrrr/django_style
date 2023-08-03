
import mysql.connector as mc
from sqlalchemy     import create_engine
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy.orm     import sessionmaker
from fastapi    import FastAPI
from pprint     import pprint


class MyAlchemy:
    def __init__(self, app: FastAPI=None, **kwargs): # type: ignore
        self.engine = None
        self.session = None
        if app is not None:
            self.init_database(app=app, **kwargs)

    def init_database(self, app:FastAPI, **kwargs):
        ''' drop & create tables '''
        cnx = mc.connect(user=kwargs.get('DATABASE_USERNAME'),                    
                         password=kwargs.get('DATABASE_PASSWORD'),
                         host=kwargs.get('DATABASE_HOSTNAME'),
                         port=kwargs.get('DATABASE_PORT'),
                         database=kwargs.get('DATABASE_NAME'))
        cursor = cnx.cursor()

        try:
            if kwargs.get('DEBUG'):
                with open('app/database/my_schema.sql', 'r') as file:
                        query = file.read()
                        cursor.execute(query, multi=True)
            else:
                pass
        except mc.Error as err:
            pprint(err.msg)
        else:
            pprint("DB initialized")
        
    
    def get_databse(self):
        ''' database session '''
        self.engine = create_engine(kwargs.get('DATABASE_URL'))  # type: ignore
        self.session = sessionmaker(autocommit=False,
                                     autoflush=False,
                                     bind=self.engine)
        if self.session is None:
            raise Exception("session not exists")
        db_session = None

        try:
            db_session = self.session()
            yield db_session
        finally:
            db_session.close()  # type: ignore

db = MyAlchemy()
base = declarative_base()
