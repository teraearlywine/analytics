{{
    config(
        schema='dimensions'
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
      , quantity 
      , fk_customer_id
      , fk_product_stock_code_id
FROM    {{ ref('stg__transaction_facts') }} -- treating as 'source' for the example 