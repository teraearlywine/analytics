{{
    config(
        materialized='table',
        dataset='cowgirl_ai'
    )
}}

SELECT  *
FROM    {{ source('source', '50_wineries_california_other_attributes') }}