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
- The marketing team, who drive traffic to the site through paid ads, email, and organic search.
- The customer success team, who build relationships with existing customers and handle their concerns.
- The product team, who builds and manages the website.
- The analytics and data science team (your teammates), who do in depth analyses and reporting for the same stakeholders.
*/

WITH staging_segments_cte AS (
    SELECT  cus.*
          , NTILE(4) OVER (ORDER BY latest_order_dt) AS recency
          , NTILE(4) OVER (ORDER BY orders) AS frequency
          , NTILE(4) OVER (ORDER BY order_value) AS monetary
    FROM    {{ ref('fact__customer_stats') }} AS cus
)

SELECT  customer_id 
      , latest_order_dt
      , orders
      , order_value
      , recency
      , frequency
      , monetary
      , CONCAT(recency, frequency, monetary) AS rfm_segment
FROM    weighted_pref