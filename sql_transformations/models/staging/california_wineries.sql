{{
    config(
        materialized='table'
    )
}}

SELECT  * 
FROM    {{ source('source', 'generate_list_100_california_wineries_type_wine_pr') }}