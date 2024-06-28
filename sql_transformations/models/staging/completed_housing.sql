{{
    config(
        materialized='table'
    )
}}

-- Alias and casting
SELECT  uuid
      , SAFE_CAST(created_ts AS TIMESTAMP) AS created_ts
      , year
      , SAFE_CAST(single_family_total AS INT64) AS single_family_total
      , SAFE_CAST(single_family_built_for_sale AS INT64) AS single_family_built_for_sale
      , SAFE_CAST(single_family_fee_simple AS INT64) AS single_family_fee_simple
      , SAFE_CAST(single_family_contractor_built AS INT64) AS single_family_contractor_built
      , SAFE_CAST(single_family_owner_built AS INT64) AS single_family_owner_built 
      , SAFE_CAST(multi_family_total AS INT64) AS multi_family_total
      , SAFE_CAST(multi_family_for_sale AS INT64) AS multi_family_for_sale
      , SAFE_CAST(multi_family_for_rent AS INT64) AS multi_family_for_rent
      , SAFE_CAST(multi_family_2_to_4_units AS INT64) AS multi_family_2_to_4_units
      , SAFE_CAST(multi_family_5_to_9_units AS INT64) AS multi_family_5_to_9_units
      , SAFE_CAST(multi_family_10_to_19_units AS INT64) AS multi_family_10_to_19_units
      , SAFE_CAST(multi_family_20_or_more_units AS INT64) AS multi_family_20_or_more_units
FROM    {{ source('source', 'completed_housing_units_annual') }}