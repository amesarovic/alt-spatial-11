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

calc_spatial_centroid_1 AS (

  {{
    alt_spatial_11.SpatialInfo_03(
      'us_states_lines', 
      [{ "name": "name", "dataType": "String" }, { "name": "geometry", "dataType": "String" }], 
      'geometry', 
      'line_string', 
      true
    )
  }}

)

SELECT *

FROM calc_spatial_centroid_1
