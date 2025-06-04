with source as (
  select distinct
    address
  from {{ ref('enriched_reviews') }}
),

with_id as (
  select
    row_number() over (order by address) as location_id,
    address
  from source
)

select * from with_id
