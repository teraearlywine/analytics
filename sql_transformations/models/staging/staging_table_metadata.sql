{{
    config(
        materialized='table',
        dataset='data_operations'
    )
}}

SELECT table_name 
FROM   teradata-development.source.INFORMATION_SCHEMA.TABLES
ORDER BY 
        table_name ASC