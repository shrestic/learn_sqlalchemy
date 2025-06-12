from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base, Column, Integer

Base = declarative_base()

Base.query = Base.query_property()


class TimeStampModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, onupdate=datetime.now(datetime.timezone.utc))
