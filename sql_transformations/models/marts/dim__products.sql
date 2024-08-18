{{
    config(
        schema='dimensions'
      , cluster_by = "pk_surrogate_key"
    )
}}


-- One record per product and product description
SELECT DISTINCT 
        {{dbt_utils.generate_surrogate_key(['fk_product_stock_code_id', 'description'])}} AS pk_surrogate_key
      , fk_product_stock_code_id AS product_id 
      , description
FROM    {{ ref('stg__transaction_facts') }} 
QUALIFY ROW_NUMBER() OVER (PARTITION BY product_id) = 1 -- 85 duplicate records found with different descriptions 
