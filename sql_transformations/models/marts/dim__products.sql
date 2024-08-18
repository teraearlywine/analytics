{{
    config(
        schema='dimensions',
        cluster_by="pk_surrogate_key"
    )
}}

-- One record per product and product description
-- Remapping product code to surrogate key to hedge against duplicates and measure 
-- product attribute changes

SELECT DISTINCT 
        {{ dbt_utils.generate_surrogate_key(['fk_product_stock_code_id', 'description']) }} AS pk_surrogate_key,
        fk_product_stock_code_id AS product_id,
        description
FROM    {{ ref('stg__transaction_facts') }} 
QUALIFY ROW_NUMBER() OVER (PARTITION BY fk_product_stock_code_id ORDER BY description) = 1 -- 85 duplicate records found with different descriptions 

-- TODO: Add logging to track the number of duplicates removed
-- TODO: Consider adding a timestamp column to track when the record was created or updated
-- TODO: Implement assertions to ensure data integrity, e.g., check for null values in critical fields
-- FIX: Ensure that the ORDER BY clause in ROW_NUMBER() is appropriate for your use case to avoid unintended results.