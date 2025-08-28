import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# Database setup
engine = create_engine('sqlite:///recipe_book.db')
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

# Import all models here
from .category import Category
from .recipe import Recipe
from .ingredient import Ingredient

def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)