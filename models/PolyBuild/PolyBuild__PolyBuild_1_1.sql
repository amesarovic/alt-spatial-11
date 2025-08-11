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

PolyBuild_1_1 AS (

  {{
    DatabricksSqlSpatial.PolyBuild(
      '02_poly_build', 
      'SequencePolyline', 
      'longitude', 
      'latitude', 
      'route_id', 
      'stop_schedule'
    )
  }}

)

SELECT *

FROM PolyBuild_1_1
