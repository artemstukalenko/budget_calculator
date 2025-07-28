import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db_engine():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", type=str, help="DB password")
    args, unknown = parser.parse_known_args()

    return create_engine(f"postgresql+psycopg2://postgres:{args.password}@localhost:5432/budget_calculator_db")

def create_db_session():
    session = sessionmaker(bind=engine)
    return session()

def get_engine():
    return engine

engine = create_db_engine()