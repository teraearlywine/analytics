SELECT  uuid
      , SAFE_CAST(created_ts AS TIMESTAMP) AS load_ts
      , SAFE_CAST(year AS STRING) AS completed_year
      , SAFE_CAST(single_family_total AS INT64) AS single_family_total
      , SAFE_CAST(single_family_built_for_sale AS INT64) AS single_family_built_for_sale
      , SAFE_CAST(single_family_contractor_built AS INT64) AS single_family_contractor_built
      , SAFE_CAST(single_family_owner_built AS INT64) AS single_family_owner_built
      , SAFE_CAST(multi_family_for_sale AS INT64) AS multi_family_for_sale
      , SAFE_CAST(multi_family_for_rent AS INT64) AS multi_family_for_rent
FROM    teradata-development.source.completed_housing_units_annual