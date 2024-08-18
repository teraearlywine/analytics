{{
    config(
        schema='dim_dbt_tera'
      , cluster_by = "pk_product_id"
    )
}}

SELECT  fk_product_stock_code_id AS pk_product_id 
      , CURRENT_DATE AS created_dt -- TODO: scd?
      , description
      , unit_price
FROM    {{ ref('stg__transaction_facts') }} -- treating as 'source' for the example 
GROUP BY 
        pk_product_id
      , description
      , unit_price