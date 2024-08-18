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

SELECT  txn.invoice_no
      , txn.invoice_dt
      , txn.fk_customer_id
      , txn.fk_product_stock_code_id
      , txn.quantity 
      , txn.unit_price -- Note: unit price sometimes changes with products
FROM    {{ ref('stg__transaction_facts') }} AS txn
