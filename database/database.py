from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:{password}@localhost/databaseName'

#Database Connected 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

#Create db session
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
