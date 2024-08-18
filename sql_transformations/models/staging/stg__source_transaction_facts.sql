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
ALIASING + CASTING
-- Assuming this is entry point for data or the source/raw foundational  layer 
-- Leaving un-refined in order to catch any future issues 

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
