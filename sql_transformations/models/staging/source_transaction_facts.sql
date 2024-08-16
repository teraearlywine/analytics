{{
    config(
        materialized='table',
        dataset='staging'
    )
}}

/*
ALIASING + CASTING

There are duplicated transaction no. TBD
Static data file has been loaded to the BQ data warehouse following 
preliminary cleaning. 

(Tera - 2024-08-16 NOTE): Column names largely ambiguous, using the definitions
from the schema in hex to clarify data model


1. transaction facts 
2. customer 
3. product detail

*/

SELECT  -- Transaction Facts
        index AS pk_id
      , invoice_date AS txn_invoice_dt  
      , invoice_no AS txn_invoice_no -- Note: this should be unique, as per definition in schema

        -- Customer Dimension - FK / Column
      , customer_id AS fk_customer_id
      , country AS customer_country

        -- Product Dimension - FK / Column
      , stock_code AS fk_product_stock_code_id
      , description AS product_description -- Note: some null values here, write a null test case
      , unit_price AS product_unit_price
      , quantity AS product_sales_per_txn
FROM    {{ source('dbt_tera', 'seed_cleaned_retail_data') }}