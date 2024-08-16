SELECT customer_id 
     , COUNT(*) AS count_records
FROM   the-data-refinery.dbt_tera.source_transactions
GROUP BY 
       customer_id 
ORDER BY 
       count_records DESC