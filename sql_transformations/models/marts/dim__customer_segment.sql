{{
    config(
        schema='dimensions'
      , partition_by = {
            "field": "latest_order_dt"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "customer_id"
    )
}}

/*
RFM: segmentation based on how recently a customer purchased an item, 
how frequently they purchase and overall order value. 

The R, F & M segments are based from 1 - 4. 
The scale is set so 1 is low (so low order value, long time since last purchase, doesn't buy a lot)
and 4 being on the higher end (high order value, recently bought and buys a lot). 
*/

WITH staging_segments_cte AS (
    SELECT  cus.*
          , NTILE(4) OVER (ORDER BY latest_order_dt) AS recency
          , NTILE(4) OVER (ORDER BY orders) AS frequency
          , NTILE(4) OVER (ORDER BY order_value) AS monetary
    FROM    {{ ref('fact__customer_stats') }} AS cus
)

SELECT  customer_id 
      , CONCAT(recency, frequency, monetary) AS rfm_segment
      , recency
      , frequency
      , monetary
      , latest_order_dt
      , orders
      , order_value
      , c.pk_surrogate_key -- mapping SCD next
      , c.customer_country
FROM    weighted_pref AS w
        LEFT JOIN {{ ref('dim__customers') }} AS c 
          ON  w.customer_id = c.customer_id
          -- AND COALESCE(c.latest_order_dt) >= c.effective_start_dt -- Hypothetical