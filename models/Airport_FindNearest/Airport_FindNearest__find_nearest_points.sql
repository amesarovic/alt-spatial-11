{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_airports_2 AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'us_airports_2') }}

),

airport_fn_01 AS (

  SELECT * 
  
  FROM {{ ref('airport_fn_01')}}

),

create_geo_point AS (

  {{ DatabricksSqlSpatial.CreatePoint('airport_fn_01', [['lon', 'lat', 'point']]) }}

),

CreatePoint_1 AS (

  {{ DatabricksSqlSpatial.CreatePoint('us_airports_2', [['lon', 'lat', 'point']]) }}

),

find_nearest_points AS (

  {{
    DatabricksSqlSpatial.FindNearest(
      ['create_geo_point', 'CreatePoint_1'], 
      'point', 
      'point', 
      'point', 
      'point', 
      100, 
      200, 
      'mls', 
      false, 
      ['city', 'state', 'name', 'lat', 'lon', 'point'], 
      ['city', 'state', 'lat', 'lon', 'iata_code', 'name', 'point']
    )
  }}

)

SELECT *

FROM find_nearest_points
