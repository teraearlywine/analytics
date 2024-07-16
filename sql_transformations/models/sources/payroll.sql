{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'payroll_schema_50_fintech_employees_bi-weekly_payp') }}