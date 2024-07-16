{{
    config(
        materialized='table'
    )
}}

SELECT  customer_id 
      , created_ts
      , email
      , phone_number
      , city
      , state
      , zipcode
      , birthdate
FROM    {{ source('source', 'dim_customer') }}