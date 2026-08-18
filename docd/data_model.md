## Data model

## News
Stores raw financial news articles/headlines entering the pipeline.

| Field | Type | Description |
|---|---|---|
| news_id | UUID | Unique identifier for news item | 
| headline | text | News headline | 
| timestamp | datetime | Time the news was published | 
| source | string | News source | 
| created_at | datetime | Time the record entered our system | 
| url | string | Article's URL | 

## Company

| Field | Type | Description |
|---|---|---|
| company_id | string | Id of the comapny | 
| company_name | string | Name of the comapny |
| ticker | string | Stock ticker associated with company | 

## News Entities
Stores companies identified in each news item.

A single news article can be associated with multiple companies.

| Field | Type | Description |
|---|---|---|
|id | UUID | Unique identifier | 
| news_id | UUID | Unique identifier for news item | 
| company_id | string | Id of the comapny | 
| confidence | float | Confidence of ticker maping |

## Sentiment
Stores sentiment analysis results for each news item.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique identifier |
| news_id | UUID | Reference to the news item |
| label | string | positive, negative, or neutral |
| score | float | Sentiment confidence/strength |
| model | string | Model used for sentiment analysis |
| processed_at | datetime | Time sentiment analysis was performed |

## Market Price
Stores raw stock-market data.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique identifier |
| ticker | string|Stock ticker associated with company |
| timestamp | datetime | Time associated with the market-price observation   |
| open | float | price at the beginning of the interval |
| high | float | highest price during the interval |
| low | float | lowest price during the interval |
| close | float | price at the end of the interval |
| volume | integer | number of shares/contracts traded |

## Sentiment Aggregate
This is derived data. It represents sentiment calculated over a specific time window.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique identifier |
| company_id | UUID | Reference to the company id |
| window_start | datetime | Start time of the sentiment aggregation window |
| window_end | datetime | End time of the sentiment aggregation window |
| window_size | string | Duration of the aggregation window, such as 5m, 15m, 1h, or 1d |
| article_count | integer | Total number of news articles associated with the company during the aggregation window |
| positive_count | integer | Number of news articles classified as positive during the aggregation window |
| negative_count | integer | Number of news articles classified as negative during the aggregation window |
| neutral_count | integer | Number of news articles classified as neutral during the aggregation window |
| average_sentiment | float | Average sentiment score of all news articles associated with the company during the aggregation window |

## Signal
This is also derived data.It represents the result of comparing sentiment with subsequent market movement

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique identifier |
| company_id | UUID | Reference to the company id |
| timestamp | datetime | Time the news was published | 
| sentiment_score | float | what the news says |
| price_change | float | what the market did |
| signal | string | our interpretation of the relationship |
| confidence | float | Confidence of ticker maping |