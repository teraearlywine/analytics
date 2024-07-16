{{
    config(
        materialized='table'
    )
}}

SELECT  employee_id
      , first_name
      , last_name
      , date_of_birth
      , gender
      , address
      , phone_number
      , email
      , hire_date
      , job_title
      , department_id
FROM    {{ source('source', 'employees') }}