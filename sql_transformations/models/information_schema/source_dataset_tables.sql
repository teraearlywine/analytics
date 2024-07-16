{{
    config(
        materialized='table'
    )
}}

SELECT table_name 
FROM   teradata-development.source.INFORMATION_SCHEMA.TABLES
ORDER BY 
        table_name ASC