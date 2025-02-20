from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from .base import Base
import datetime

class Insight(Base):
    __tablename__ = "insights"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("reddit_posts.id"))  # Links to Reddit posts
    sentiment_score = Column(Float)
    emotion_category = Column(String)
    key_phrases = Column(Text)  # JSON-encoded list of phrases
    similarity_score = Column(Float)
    ai_summary = Column(Text)
    ai_response = Column(Text)
    processed_at = Column(DateTime, default=datetime.datetime.utcnow)
