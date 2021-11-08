from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date
from datetime import date


engine = create_engine('postgresql://postgres:anup%40101@localhost:5000/test')
Session = sessionmaker(bind=engine)

Base = declarative_base()

# 3 - create a new session
session = Session()



#creating tables

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

Base.metadata.create_all(engine)



#----------------------------------------------------------------------------------
# Adding(inserting) Data into table
# 4 - create movies
# bourne_identity = Movie("The Bourne Identity xyz", date(2022, 10, 11))
# bourne_identity1 = Movie("The Bourne Identity abc", date(2012, 10, 11))

# session.add(bourne_identity)
# session.add(bourne_identity1)

# session.commit()

#--------------------------------------------------------------------------------------

#Reading data from the table 
movies = session.query(Movie).all()

# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

session.close()