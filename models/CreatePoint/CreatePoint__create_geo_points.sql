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

create_geo_points AS (

  {{
    DatabricksSqlSpatial.CreatePoint(
      'points_02', 
      [['start_long', 'start_lat', 'start_point'], ['destination_long', 'destination_lat', 'dst_point']]
    )
  }}

)

SELECT *

FROM create_geo_points
