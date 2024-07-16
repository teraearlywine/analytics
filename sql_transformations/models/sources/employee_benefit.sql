{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'employee_benefit_schema_50_fintech_employees') }}