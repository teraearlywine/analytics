{{
    config(
        materialized='table'
    )
}}

SELECT  job_id 
      , job_title
      , description 
      , level
      , department
      , salary_budget
FROM    {{ source('source', 'fintech_jobs') }}