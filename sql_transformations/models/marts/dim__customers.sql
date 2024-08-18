{{
    config(
        schema='dimensions'
      , partition_by = {
            "field": "created_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "pk_surrogate_key"
    )
}}

-- One record for every customer and country of residence
SELECT  DISTINCT 
        {{dbt_utils.generate_surrogate_key(['fk_customer_id', 'customer_country'])}} AS pk_surrogate_key
      , fk_customer_id AS customer_id 
      , customer_country 
      , CURRENT_DATE AS created_dt
      , '' AS city
      , '' AS zip_code
FROM    {{ ref('stg__transaction_facts') }} -- treating as 'source' for the example 
