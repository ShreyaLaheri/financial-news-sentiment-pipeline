# Financial News Sentiment & Stock Movement Pipeline

An end-to-end data engineering and NLP pipeline that continuously ingests financial news, analyzes sentiment, maps news to relevant stock tickers, aggregates sentiment over time, and compares sentiment against actual stock price movements.

## Project Overview

The pipeline will:

1. Ingest live or simulated financial news.
2. Process news through a streaming pipeline using Apache Kafka.
3. Analyze financial sentiment using a finance-focused NLP model.
4. Identify companies mentioned in each news article.
5. Map companies to their stock tickers.
6. Aggregate sentiment across different time windows.
7. Retrieve historical and market price data.
8. Align news sentiment with subsequent stock price movements.
9. Generate analytical signals based on sentiment and price behavior.
10. Expose processed data through a FastAPI backend.
11. Visualize news, sentiment, prices, and signals through an interactive dashboard.

## Architecture

```text
Financial News
      │
      ▼
Kafka Producer
      │
      ▼
Kafka Topic
      │
      ▼
Stream Processor
      │
      ├── Sentiment Analysis
      ├── Company Extraction
      └── Ticker Mapping
      │
      ▼
PostgreSQL
      │
      ├───────────────┐
      ▼               ▼
Sentiment         Market Data
Aggregation       (yfinance)
      │               │
      └───────┬───────┘
              ▼
       Signal Analysis
              │
              ▼
           FastAPI
              │
              ▼
         Dashboard