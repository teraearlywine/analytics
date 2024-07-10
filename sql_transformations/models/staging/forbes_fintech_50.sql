{{
    config(
        materialized='table'
    )
}}

-- not ai generated data, scraped from website
SELECT  company_name
      , industry
      , funding
      , location
FROM    {{ source('source', 'forbes_fintech_50')}}