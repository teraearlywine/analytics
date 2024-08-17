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
        index AS pk_id                  -- PK surrogate key 
      , invoice_date AS txn_invoice_dt  -- Note: NOT unique, however is immutable
      , invoice_no AS txn_invoice_no    -- Note: NOT unique, however is immutable

        -- Customer Dimension - FK / Column
      , customer_id AS fk_customer_id
      , country AS customer_country

        -- Product Dimension - FK / Column
      , stock_code AS fk_product_stock_code_id
      , description AS product_description -- Note: some null values here, write a null test case
      , unit_price AS product_unit_price
      , quantity AS product_sales_per_txn
FROM    {{ source('dbt_tera', 'seed_cleaned_retail_data') }}


-- SELECT * 
-- FROM    the-data-refinery.dbt_tera_staging.source_transaction_facts
-- WHERE   txn_invoice_no = "561873" -- 284452, 284437 are duplicates, first validate this as a 'true' duplicate with team
-- ORDER BY fk_product_stock_code_id
-- GROUP BY 1,2 
