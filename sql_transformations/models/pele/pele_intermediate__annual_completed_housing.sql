{{
    config(
        schema='pele_intermediate',
        materialized='table',
        partition_by = {
            "field": "created_ts"
          , "data_type": "date"
          , "granularity": "month"
        }
      , cluster_by = "uuid"
    )
}}

SELECT  *
FROM    {{ ref('annual_completed_housing') }}