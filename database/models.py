import uuid 
from sqlalchemy import Column, String, DateTime, Text, Float, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class News(Base):
    __tablename__ = "news"
    news_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    headline = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    source = Column(String(80), nullable=False)
    created_at = Column(DateTime, nullable=False)
    url = Column(Text, nullable=False, unique=True)

# ---------------- # Relationships #  ---------------- #
    news_entities = relationship( "NewsEntity", back_populates="news", cascade="all, delete-orphan") 
    sentiments = relationship( "Sentiment", back_populates="news", cascade="all, delete-orphan") 

class Company(Base):
    __tablename__ = "companies"
    company_id = Column(String(50), primary_key=True)
    company_name = Column(String(200), nullable=False)
    ticker = Column(String(20), nullable=False, unique = True, index = True)

# ---------------- # Relationships #  ---------------- #
    news_entities = relationship( "NewsEntity", back_populates="company") 
    market_prices = relationship( "MarketPrice", back_populates="company") 
    sentiment_aggregates = relationship( "SentimentAggregate", back_populates="company") 
    signals = relationship( "Signal", back_populates="company")

class NewsEntity(Base):
    __tablename__ = "news_entities"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    news_id = Column(UUID(as_uuid=True), ForeignKey("news.news_id"), nullable=False, index = True)
    company_id = Column(String(50), ForeignKey("companies.company_id"), nullable=False, index = True)
    confidence = Column(Float, nullable=False)

# ---------------- # Relationships #  ---------------- #
    news = relationship( "News", back_populates="news_entities") 
    company = relationship( "Company", back_populates="news_entities") 

class Sentiment(Base):
    __tablename__ = "sentiments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    news_id = Column(UUID(as_uuid=True), ForeignKey("news.news_id"), nullable=False, index = True)
    label = Column(String(20), nullable=False)
    score = Column(Float, nullable=False)
    model = Column(String(80), nullable=False)
    processed_at = Column(DateTime, nullable=False)

# ---------------- # Relationships #  ---------------- #
    news = relationship( "News", back_populates="sentiments")


class MarketPrice(Base):
    __tablename__ = "market_prices"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = Column(String(50), ForeignKey("companies.company_id"), nullable=False, index = True)
    timestamp = Column(DateTime, nullable=False, index = True)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

# ---------------- # Relationships #  ---------------- #
    company = relationship( "Company", back_populates="market_prices") 


class SentimentAggregate(Base):
    __tablename__ = "sentiment_aggregates"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = Column(String(50), ForeignKey("companies.company_id"), nullable=False, index = True)
    window_start = Column(DateTime, nullable=False)
    window_end = Column(DateTime, nullable=False)
    window_size = Column(String(15), nullable=False)
    article_count = Column(Integer, nullable=False)
    positive_count = Column(Integer, nullable=False)
    negative_count = Column(Integer, nullable=False)
    neutral_count = Column(Integer, nullable=False)
    average_sentiment = Column(Float, nullable=False)

# ---------------- # Relationships #  ---------------- #
    company = relationship( "Company", back_populates="sentiment_aggregates") 

class Signal(Base):
    __tablename__ = "signals"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = Column(String(50), ForeignKey("companies.company_id"), nullable=False, index = True)
    timestamp = Column(DateTime, nullable=False, index = True)
    sentiment_score = Column(Float, nullable=False)
    price_change = Column(Float, nullable=False)
    signal = Column(String(50), nullable=False)
    confidence = Column(Float, nullable=False)

# ---------------- # Relationships #  ---------------- #
    company = relationship( "Company", back_populates="signals")

