{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'employee_schema_fintech_company_50_employees_add_s') }}