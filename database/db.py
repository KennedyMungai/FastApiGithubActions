"""The database file"""
import os

import pymysql
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(find_dotenv())

MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_PORT = os.environ.get("MYSQL_PORT")

MYSQL_URL = f"mysql+pymysql://{MYSQL_USER}@{MYSQL_PASSWORD}:{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(MYSQL_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    """The database dependency"""
    _db = SessionLocal()
    
    try:
        yield _db
    finally:
        _db.close()