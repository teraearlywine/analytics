{{
    config(
        partition_by = {
            "field": "invoice_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "pk_id"
    )
}}

/*
ALIASING + PRE-PROCESSING

TODO: 
- validate double orders in a day, handful of quantity differences
- check with team on Manual

If either of these map to certain product features/are actually relevant,
we'd want to add a flag to capture these records before deduplicating

1. Transaction Facts 
2. Customer Dimension 
3. Product Dimension
*/

SELECT  index AS pk_id -- PK surrogate key 
      , invoice_date AS invoice_dt 
      , invoice_no AS invoice_no   
      , customer_id AS fk_customer_id           -- Customer Dimension - FK / Column
      , country AS customer_country             
      , stock_code AS fk_product_stock_code_id  -- Product Dimension - FK / Column
      , COALESCE(description, "NULL-PLACEHOLDER") AS description -- (Tera - 2024-08-16 NOTE): null values here, found due to test case
      , unit_price
      , quantity
FROM    {{ source('dbt_tera', 'seed_cleaned_retail_data') }}
WHERE   customer_id != 0 -- A handful of customer IDs had 0, this could be a bug, but generally customers who've purchased should have id
        AND quantity >= 0   -- 143,985 negative values. Could be return, but factoring out to get only positive numbers
        AND unit_price != 0.0
        AND description != 'Manual'
QUALIFY ROW_NUMBER() OVER (PARTITION BY invoice_no, fk_customer_id, fk_product_stock_code_id ORDER BY invoice_dt DESC) = 1