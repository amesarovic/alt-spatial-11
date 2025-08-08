{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH poly_build AS (

  SELECT * 
  
  FROM {{ ref('poly_build')}}

),

Polygon AS (

  {{
    DatabricksSqlSpatial.PolyBuild(
      'poly_build', 
      'SequencePolygon', 
      'longitude', 
      'latitude', 
      'route_id', 
      'stop_schedule'
    )
  }}

)

SELECT *

FROM Polygon
