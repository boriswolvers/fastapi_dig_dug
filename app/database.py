from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote  
from .config import settings

#engine = create_engine('mysql+mysqlconnector://user_name:%s@localhost:3306/database' % quote('your_password'))

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:%s@{settings.database_hostname}:{settings.database_port}/{settings.database_name}' % quote(settings.database_password)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
