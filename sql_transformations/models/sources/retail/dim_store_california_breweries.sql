{{
    config(
        materialized='table'
    )
}}

SELECT  store_id
      , store_number
      , store_name
      , store_street_address
      , store_city
      , store_state
      , store_zipcode
FROM    {{ source('source', 'dim_store_california_breweries') }}