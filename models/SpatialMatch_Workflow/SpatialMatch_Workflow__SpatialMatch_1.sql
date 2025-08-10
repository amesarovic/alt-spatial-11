{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH Stores AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_raw_1')}}

),

Store AS (

  {{ DatabricksSqlSpatial.CreatePoint('Stores', [['store_lon', 'store_lat', 'store_location']]) }}

),

Zones AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_2')}}

),

Zone AS (

  {{ DatabricksSqlSpatial.PolyBuild('Zones', 'SequencePolygon', '', '', '', '') }}

),

SpatialMatch_1 AS (

  {{
    DatabricksSqlSpatial.SpatialMatch(
      ['Store', 'Zone'], 
      [
        ['store_id', 'store_name', 'store_lat', 'store_lon', 'store_type', 'store_location'], 
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
