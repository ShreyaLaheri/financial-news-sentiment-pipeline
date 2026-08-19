from datetime import datetime
from sqlalchemy.orm import sessionmaker
from database.connection import engine
from database.models import Company, News, NewsEntity, Sentiment

# ============================================================
# Database Session
# ============================================================
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


try:
    # ========================================================
    # 1. Get or Create Company
    # ========================================================
    company = session.query(Company).filter_by(
        company_id="NVDA"
    ).first()

    if company is None:
        company = Company(
            company_id="NVDA",
            company_name="NVIDIA",
            ticker="NVDA"
        )
        session.add(company)
        session.flush()
        print("Company created.")

    else:
        print("Company already exists.")


    # ========================================================
    # 2. Get or Create News
    # ========================================================
    news = session.query(News).filter_by(
        url="https://example.com/nvidia-ai-chip"
    ).first()

    if news is None:
        news = News(
            headline="NVIDIA announces new AI chip",
            timestamp=datetime.now(),
            source="Reuters",
            created_at=datetime.now(),
            url="https://example.com/nvidia-ai-chip"
        )
        session.add(news)
        session.flush()
        print("News created.")

    else:
        print("News already exists.")


    # ========================================================
    # 3. Get or Create NewsEntity
    # ========================================================
    news_entity = session.query(NewsEntity).filter_by(
        news_id=news.news_id,
        company_id=company.company_id
    ).first()
    if news_entity is None:
        news_entity = NewsEntity(
            news_id=news.news_id,
            company_id=company.company_id,
            confidence=0.98
        )
        session.add(news_entity)
        print("News entity created.")

    else:
        print("News entity already exists.")


    # ========================================================
    # 4. Get or Create Sentiment
    # ========================================================
    sentiment = session.query(Sentiment).filter_by(
        news_id=news.news_id,
        model="FinBERT"
    ).first()

    if sentiment is None:
        sentiment = Sentiment(
            news_id=news.news_id,
            label="positive",
            score=0.94,
            model="FinBERT",
            processed_at=datetime.now()
        )
        session.add(sentiment)
        print("Sentiment created.")

    else:
        print("Sentiment already exists.")


    # ========================================================
    # 5. Commit Everything
    # ========================================================
    session.commit()
    print("\nSeed data completed successfully!")


except Exception as e:
    session.rollback()
    print("\nError while inserting seed data:")
    print(e)


finally:
    session.close()