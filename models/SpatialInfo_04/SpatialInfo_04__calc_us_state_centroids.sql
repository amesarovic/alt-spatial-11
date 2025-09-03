{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_states AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'us_states') }}

),

calc_us_state_centroids AS (

  {{
    alt_spatial_11.SpatialInfo_04(
      'us_states', 
      [
        { "name": "name", "dataType": "String" }, 
        { "name": "distance", "dataType": "Integer" }, 
        { "name": "geometry", "dataType": "String" }
      ], 
      'geometry', 
      'Polygon', 
      true
    )
  }}

)

SELECT *

FROM calc_us_state_centroids
