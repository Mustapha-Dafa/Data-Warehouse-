with raw as (
  select * from {{ source('public', 'review') }}
),

cleaned as (
  select distinct on (review_text, address)
   md5(
      coalesce(lower(regexp_replace(review_text, '[^\w\s]', '', 'g')), '') ||
      coalesce(review_date::text, '') ||
      coalesce(address, '')
    ) as review_key,
    case
      when lower(bank_name) like '%cih%' then 'CIH BANK'
      when lower(bank_name) like '%barid%' then 'AL BARID BANK'
      when lower(bank_name) ~ 'attijari|wafa' then 'ATTIJARIWAFA BANK'
      when lower(bank_name) like '%chaabi%' or lower(bank_name) like '%populaire%' or lower(bank_name) like '%bp%' then 'BANQUE POPULAIRE'
      when lower(bank_name) like '%bmce%' or lower(bank_name) like '%bank of africa%' then 'BMCE BANK'
      when lower(bank_name) like '%umnia%' then 'UMNIA BANK'
      when lower(bank_name) like '%bank al yousr%' or lower(bank_name) like '%al yousr%' then 'AL YOUSR BANK'
      when lower(bank_name) like '%assaafa%' or lower(bank_name) like'%assafa%' or lower(bank_name) like '%dar assafaa%' or lower(bank_name) like '%bank assafa%' then 'ASSAFA BANK'
      when lower(bank_name) like '%dar al amane%' then 'DAR AL AMANE'
      when lower(bank_name) like '%akhdar%' then 'AL AKHDAR BANK'
      when lower(bank_name) like '%cfg%' then 'CFG BANK'
      when lower(bank_name) like '%citi%' then 'CITI BANK'
      when lower(bank_name) like '%societe generale%' or lower(bank_name) like '%sgmb%' then 'SOCIETE GENERALE'
      when lower(bank_name) like '%credit agricole%' then 'CRÉDIT AGRICOLE'
      else upper(bank_name)
    end as bank_name,
    address ,
    lower(regexp_replace(review_text, '[^\w\s]', '', 'g')) as review_text,
    rating,
    review_date
  from raw
  where 
      review_text is not null 
      and rating is not null
      and lower(regexp_replace(review_text, '[^\w\s]', '', 'g')) <>''
      and address  ilike '%morocco%'
)

select * from cleaned


