{{
    config(
        materialized='table'
    )
}}

SELECT  employee_benefit_id
      , employee_id
      , benefit_id
      , benefit_start_date
      , benefit_end_date
FROM    {{ source('source', 'employee_benefits') }}