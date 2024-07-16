{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'department_schema_fintech_company_records_added') }}