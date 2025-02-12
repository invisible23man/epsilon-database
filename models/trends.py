from sqlalchemy import Column, Integer, String, Float, DateTime
from .base import Base
import datetime

class TrendData(Base):
    __tablename__ = "trend_data"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    sentiment_score = Column(Float)
    source = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    raw_data = Column(String)
