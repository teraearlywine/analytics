{{
    config(
        dataset='staging',
        materialized='table',
        persist_docs={
            "relation": true, 
            "columns": true
        }
    )
}}

SELECT  job_id 
      , job_title
      , description 
      , level
      , department
      , salary_budget
FROM    {{ ref( 'fintech_jobs' )}}