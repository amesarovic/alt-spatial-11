{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH Center AS (

  SELECT * 
  
  FROM {{ ref('find_nearest_raw_2')}}

),

Customer AS (

  SELECT * 
  
  FROM {{ ref('find_nearest_raw_1')}}

),

create_geo_point AS (

  {{ DatabricksSqlSpatial.CreatePoint('Customer', [['lon', 'lat', 'point']]) }}

),

create_geo_point_1 AS (

  {{ DatabricksSqlSpatial.CreatePoint('Center', [['lon', 'lat', 'point']]) }}

),

FindNearestPoints AS (

  {{
    DatabricksSqlSpatial.FindNearest(
      ['create_geo_point', 'create_geo_point_1'], 
      'point', 
      'center_id', 
      'point', 
      'point', 
      3, 
      20, 
      'kms', 
      false, 
      ['customer_id', 'lat', 'lon', 'point'], 
      ['center_id', 'lat', 'lon', 'point']
    )
  }}

)

SELECT *

FROM FindNearestPoints
