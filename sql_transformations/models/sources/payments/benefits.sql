{{
    config(
        materialized='table'
    )
}}

-- base table is actually for benefits, yes IK. working on it..
SELECT  benefit_id
      , benefit_name
      , benefit_description
      , benefit_cost
FROM    {{ source('source', 'employee_benefit_schema_50_employees_fintech_compa') }}