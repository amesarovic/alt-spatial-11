{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH points_02 AS (

  SELECT * 
  
  FROM {{ ref('points_02')}}

),

CreatePoint_1 AS (

  {{ DatabricksSqlSpatial.CreatePoint('points_02', [['start_long', 'start_lat', 'point']]) }}

),

buffer_points AS (

  {{
    alt_spatial_11.Buffer_01(
      'CreatePoint_1', 
      [
        { "name": "start_city", "dataType": "String" }, 
        { "name": "start_lat", "dataType": "Decimal" }, 
        { "name": "start_long", "dataType": "Decimal" }, 
        { "name": "destination_city", "dataType": "String" }, 
        { "name": "destination_lat", "dataType": "Decimal" }, 
        { "name": "destination_long", "dataType": "Decimal" }, 
        { "name": "point", "dataType": "String" }
      ], 
      'point', 
      'output', 
      10, 
      'miles'
    )
  }}

)

SELECT *

FROM buffer_points
