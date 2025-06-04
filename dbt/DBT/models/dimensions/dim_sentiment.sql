with values as (
  select unnest(array['Positive', 'Neutral', 'Negative']) as sentiment_label
),

with_id as (
  select
    row_number() over (order by sentiment_label) as sentiment_id,
    sentiment_label
  from values
)

select * from with_id
