from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


db = create_engine("sqlite:///banco.db")

base = declarative_base()

class Usuario(base):
    

