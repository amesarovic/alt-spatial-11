{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH `02_poly_build` AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'poly_build_02') }}

),

build_route_polygon AS (

  {{
    DatabricksSqlSpatial.PolyBuild(
      '02_poly_build', 
      'SequencePolygon', 
      'longitude', 
      'latitude', 
      'route_id', 
      'stop_schedule'
    )
  }}

)

SELECT *

FROM build_route_polygon
