with base as (
  select * from {{ ref('enriched_reviews') }}
),

joined as (
  select
    base.review_key,
    base.rating,
    base.review_date,
    b.bank_id,
    l.location_id,
    s.sentiment_id
  from base
  left join {{ ref('dim_bank') }} b on base.bank_name = b.bank_name
  left join {{ ref('dim_location') }} l on base.address = l.address
  left join {{ ref('dim_sentiment') }} s on base.sentiment = s.sentiment_label
)

select * from joined
