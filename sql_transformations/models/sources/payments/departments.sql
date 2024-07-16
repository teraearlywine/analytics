{{
    config(
        materialized='table'
    )
}}

SELECT  department_id
      , department_name
      , manager_id
FROM    {{ source('source', 'department_schema_fintech_company_records_added') }}