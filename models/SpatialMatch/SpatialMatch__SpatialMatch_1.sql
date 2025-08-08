{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH spatial_match_1 AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_1')}}

),

spatial_match_2 AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_2')}}

),

SpatialMatch_1 AS (

  {{
    DatabricksSqlSpatial.SpatialMatch(
      ['spatial_match_1', 'spatial_match_2'], 
      [
        ['store_id', 'store_name', 'store_location', 'store_type'], 
        ['zone_id', 'zone_name', 'zone_polygon', 'delivery_fee']
      ], 
      '', 
      '', 
      ''
    )
  }}

)

SELECT *

FROM SpatialMatch_1
