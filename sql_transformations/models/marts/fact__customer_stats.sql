{{
    config(
        schema='facts'
      , partition_by = {
            "field": "latest_order_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "customer_id"
    )
}}

-- Base customer order stats
-- Used for establishing R x F x M score

WITH customer_cte AS (
    SELECT  fk_customer_id AS customer_id 
          , MAX(invoice_dt) AS latest_order_dt 
          , COUNT(DISTINCT fk_product_stock_code_id) AS orders 
          , ROUND(SUM(unit_price * quantity), 2) AS order_value
    FROM    {{ ref('fact__transactions') }} AS txn
    GROUP BY   
            customer_id
)

SELECT  customer_id 
      , latest_order_dt
      , orders
      , order_value
FROM    customer_cte