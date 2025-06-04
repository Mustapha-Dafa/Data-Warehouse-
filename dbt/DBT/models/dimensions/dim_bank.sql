with source as (
  select distinct
    bank_name
  from {{ ref('enriched_reviews') }}
),

with_id as (
  select
    row_number() over (order by bank_name) as bank_id,
    bank_name
  from source
)

select * from with_id
