{{
    config(
        materialized='table'
    )
}}

SELECT  breed
      , purpose 
      , egg_production_per_year
      , egg_color
      , temperament
      , size
FROM    {{ source('source', 'generate_list_chicken_breeds_their_purpose_other_a') }}