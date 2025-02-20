from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from .base import Base
import datetime

class RedditPost(Base):  # Updated class name for clarity
    __tablename__ = "reddit_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(Text)  # Full Reddit post content
    subreddit = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    upvotes = Column(Integer)
    comments = Column(Integer)
    processed = Column(Boolean, default=False)  # New field
