{{
    config(
        materialized='table'
    )
}}

SELECT  *
FROM    {{ source('source', '50_wineries_california_other_attributes') }}