{{
    config(
        schema='dimensions'
      , cluster_by = "product_id"
    )
}}


-- One record per product ID and unit price
SELECT DISTINCT 
        {{dbt_utils.generate_surrogate_key(['product_id', 'unit_price'])}} AS pk_surrogate_key
      , fk_product_stock_code_id AS product_id 
      , description
      , unit_price
FROM    {{ ref('stg__transaction_facts') }} -- treating as 'source' for the example 