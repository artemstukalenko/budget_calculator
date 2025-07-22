import argparse

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bc_core import HistoryRecord

parser = argparse.ArgumentParser()
parser.add_argument("--password", type=str, help="DB password")
args, unknown = parser.parse_known_args()

DATABASE_URL = f"postgresql+psycopg2://postgres:{args.password}@localhost:5432/budget_calculator_db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class HistoryRecordModel(Base):
    __tablename__ = "history"


    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    total_uah = Column(Numeric)
    total_usd = Column(Numeric)
    total_liq_uah = Column(Numeric)
    total_liq_usd = Column(Numeric)
    liquid_percent = Column(Numeric)
    interest_rate_percent = Column(Numeric)
    exposure_table = Column(String)


def persist(history_record: HistoryRecord):
    model = HistoryRecordModel(
        date=history_record.date,
        total_uah=history_record.total_uah,
        total_usd=history_record.total_usd,
        total_liq_uah=history_record.total_liq_uah,
        total_liq_usd=history_record.total_liq_usd,
        liquid_percent=history_record.liquid_percent,
        interest_rate_percent=history_record.interest_rate_percent,
        exposure_table=str(history_record.exposure_table)
    )

    session.add(model)
    session.commit()
    print(f"Saved history record with id: {model.id}")