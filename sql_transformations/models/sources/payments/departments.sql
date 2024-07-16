{{
    config(
        materialized='table'
    )
}}

SELECT  department_id
      , department_name
      , manager_id
FROM    {{ source('source', 'departments') }}