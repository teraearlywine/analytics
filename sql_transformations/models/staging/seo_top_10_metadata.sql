{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'top_10_seo_pages_their_metadata_description_keywor') }}