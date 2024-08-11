from sqlalchemy import create_engine

engine = create_engine("sqlite:///xddDB.db")
engine.connect()