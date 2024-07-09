{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'top_50_seo_webpages_their_attributes') }}