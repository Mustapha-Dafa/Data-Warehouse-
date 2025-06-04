with base as (
  select * from {{ ref('clean_reviews') }}
),
sentiment as (
  select * from {{ source('public', 'sentiment_lang') }}
)
select
  base.*,
  sentiment.language,
  sentiment.sentiment
from base
left join sentiment on base.review_key = sentiment.review_key