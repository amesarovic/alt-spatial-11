{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_states_lines AS (

  SELECT * 
  
  FROM {{ ref('us_states_lines')}}

),

SpatialInfo_04_1_1 AS (

  {{
    alt_spatial_11.SpatialInfo_04(
      'us_states_lines', 
      [{ "name": "name", "dataType": "String" }, { "name": "geometry", "dataType": "String" }], 
      'geometry', 
      'LineString', 
      true
    )
  }}

)

SELECT *

FROM SpatialInfo_04_1_1
