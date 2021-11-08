from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.Schemas import *
 
engine = create_engine('postgresql://postgres:anup%40101@localhost:5000/test')
Session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)