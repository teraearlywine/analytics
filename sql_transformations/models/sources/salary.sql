{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'salary_schema_50_fintech_employees') }}