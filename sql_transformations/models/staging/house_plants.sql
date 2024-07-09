{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'generate_list_100_house_plants_type_other_attribut') }}