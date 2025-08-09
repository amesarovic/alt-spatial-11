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

CreatePoint AS (

  {{
    DatabricksSqlSpatial.CreatePoint(
      'points_02', 
      [['start_long', 'start_lat', 'start_point'], ['destination_long', 'destination_lat', 'dest_point']]
    )
  }}

),

Distance AS (

  {{
    DatabricksSqlSpatial.Distance(
      'CreatePoint', 
      'start_point', 
      'dest_point', 
      'point', 
      'point', 
      true, 
      'kms', 
      true, 
      false, 
      [
        'start_city', 
        'start_lat', 
        'start_long', 
        'destination_city', 
        'destination_lat', 
        'destination_long', 
        'start_point', 
        'dest_point'
      ]
    )
  }}

)

SELECT *

FROM Distance
