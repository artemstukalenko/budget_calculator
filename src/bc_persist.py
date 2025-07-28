from decimal import Decimal

from sqlalchemy.orm import declarative_base
from bc_db_connect import create_db_session
from bc_core import HistoryRecord

session = create_db_session()
Base = declarative_base()

def persist(history_record: HistoryRecord):
    model = HistoryRecord(
        date=history_record.date,
        total_uah=history_record.total_uah,
        total_usd=history_record.total_usd,
        total_liq_uah=history_record.total_liq_uah,
        total_liq_usd=history_record.total_liq_usd,
        liquid_percent=history_record.liquid_percent,
        interest_rate_percent=history_record.interest_rate_percent,
        exposure_table=str(transform_exposures(history_record.exposure_table))
    )

    session.add(model)
    session.commit()
    print(f"Saved history record with id: {model.id}")


def transform_exposures(exposure_table: dict[str, Decimal]) -> dict[str, float]:
    return {k: float(v) for k, v in exposure_table.items()}