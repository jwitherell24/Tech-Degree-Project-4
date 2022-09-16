from venv import create
from sqlalchemy import (create_engine, Column,
                        Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

engine = create_engine("sqlite:///inventory.db, echo=False")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = "products"