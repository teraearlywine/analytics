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

SELECT  uuid
      , created_ts
      , year
      , ARRAY_AGG(
            STRUCT(
                single_family_total
              , single_family_built_for_sale
              , single_family_fee_simple
              , single_family_contractor_built
              , single_family_owner_built
            ) ORDER BY year
      ) AS single_family
      , ARRAY_AGG(
            STRUCT(
                  multi_family_total
                , multi_family_for_sale
                , multi_family_for_rent
                , multi_family_2_to_4_units
                , multi_family_5_to_9_units
                , multi_family_10_to_19_units
                , multi_family_20_or_more_units
            ) ORDER BY year
      ) AS multi_family
FROM  {{ ref('annual_completed_housing') }}
GROUP BY 
      uuid
    , created_ts
    , year