import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from secret import LOCAL_DB
SQLALCHEMY_DATABASE_URL = LOCAL_DB

# heroku_db = os.environ.get('DATABASE_URL')
# SQLALCHEMY_DATABASE_URL = heroku_db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()