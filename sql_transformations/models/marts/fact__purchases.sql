{{
    config(
        schema='facts'
      , partition_by = {
            "field": "invoice_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "invoice_no"
    )
}}

SELECT  invoice_no
      , invoice_dt
      , fk_customer_id
      , fk_product_stock_code_id
      , quantity 
      , unit_price -- Note: unit price sometimes changes with products
FROM    {{ ref('stg__transaction_facts') }} -- treating as 'source' for the example 
