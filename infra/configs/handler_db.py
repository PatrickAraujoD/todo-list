from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs import configs_env

class HandlerDb:
  def __init__(self):
    self.__connection_url = configs_env["database_url"]
    self.session = None
  
  def getEngine(self):
    engine = create_engine(self.__connection_url)
    return engine
  
  def __enter__(self):
    engine = create_engine(self.__connection_url)
    session_maker = sessionmaker()
    self.session = session_maker(bind=engine)
    return self

  def __exit__(self, exc_type, exc_value, trace):
    self.session.close()