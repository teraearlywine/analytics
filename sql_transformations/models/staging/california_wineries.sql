{{
    config(
        materialized='table'
    )
}}

SELECT  winery_name 
      , grape_varietal
      , location 
      , rating
      , price_range
FROM    {{ source('source', 'list_top_100_wineries_california_grape_varietal_ot') }}