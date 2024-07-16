{{
    config(
        materialized='table'
    )
}}

SELECT  product_id
      , sku_number
      , product_description
      , category_type
      , brand_name
      , department_name
      , store_id
FROM    {{ source('source', 'dim_products') }}