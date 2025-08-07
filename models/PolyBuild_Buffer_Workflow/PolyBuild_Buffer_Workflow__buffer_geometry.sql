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

PolyBuild_1 AS (

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

),

buffer_geometry AS (

  {{
    alt_spatial_11.Buffer_01(
      'PolyBuild_1', 
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

FROM buffer_geometry
