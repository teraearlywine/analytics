{{
    config(
        schema='pele',
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
FROM    {{ ref('pele_intermediate__annual_completed_housing') }}