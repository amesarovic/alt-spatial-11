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

LineString AS (

  {{
    DatabricksSqlSpatial.PolyBuild(
      'poly_build', 
      'SequencePolyline', 
      'longitude', 
      'latitude', 
      'route_id', 
      'stop_schedule'
    )
  }}

),

LineString_Buffer AS (

  {{
    alt_spatial_11.Buffer_01(
      'LineString', 
      [
        { "name": "grouping_column_name", "dataType": "String" }, 
        { "name": "geometry_wkt", "dataType": "String" }
      ], 
      'geometry_wkt', 
      'output', 
      200, 
      'meters'
    )
  }}

)

SELECT *

FROM LineString_Buffer
