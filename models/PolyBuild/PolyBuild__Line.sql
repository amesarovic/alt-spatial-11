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

Line AS (

  {{
    DatabricksSqlSpatial.PolyBuild(
      'poly_build', 
      'SequencePolyline', 
      'longitude', 
      'latitude', 
      'stop_schedule', 
      'stop_schedule'
    )
  }}

)

SELECT *

FROM Line
