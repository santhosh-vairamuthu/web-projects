from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# This line creates an SQLAlchemy engine to interact with the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# This line creates a sessionmaker, which is used to create individual sessions for interacting with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This line creates a base class for your SQLAlchemy models.
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
