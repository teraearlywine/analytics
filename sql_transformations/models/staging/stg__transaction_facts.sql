{{
    config(
        partition_by = {
            "field": "invoice_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "invoice_no"
    )
}}

/*
Deduplicating / Refining

TODO: 
- validate double orders in a day, handful of quantity differences
- check with team on Manual

If either of these map to certain product features/are actually relevant,
we'd want to add a flag to capture these records before deduplicating

*/

SELECT  pk_id
      , invoice_dt
      , invoice_no
      , fk_customer_id
      , customer_country
      , fk_product_stock_code_id
      , description
      , unit_price
      , quantity
FROM    {{ ref('stg__source_transaction_facts') }}
WHERE   fk_customer_id != 0 -- A handful of customer IDs had 0, this could be a bug, but generally customers who've purchased should have id
        AND quantity >= 0   -- 143,985 negative values. Could be return, but factoring out to get only positive numbers
        AND unit_price != 0.0
        AND description != 'Manual'
QUALIFY ROW_NUMBER() OVER (PARTITION BY invoice_no ORDER BY invoice_dt DESC) = 1