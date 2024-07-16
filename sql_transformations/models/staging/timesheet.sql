{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'timesheet_schema_50_fintech_employees_3_months_pai') }}