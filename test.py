from database.services import *
from database.base import Base, engine, Session
Base.metadata.create_all(engine)
add_to_cart(2)