{{
    config(
        
        partition_by = {
            "field": "created_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "pk_customer_id"
    )
}}

SELECT  fk_customer_id AS pk_customer_id 
      , CURRENT_DATE AS created_dt
      , customer_country 
      , '' AS city
      , '' AS zip_code
FROM    {{ ref('stg__transaction_facts') }} -- treating as 'source' for the example 
GROUP BY 
        pk_customer_id 
      , customer_Country
      , city
      , zip_code