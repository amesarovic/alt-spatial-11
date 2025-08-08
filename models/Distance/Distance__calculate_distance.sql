{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH distances AS (

  SELECT * 
  
  FROM {{ ref('distances')}}

),

calculate_distance AS (

  {{
    DatabricksSqlSpatial.Distance(
      'distances', 
      'source_point', 
      'dest_point', 
      'point', 
      'point', 
      true, 
      'kms', 
      true, 
      true, 
      ['start_city', 'destination_city', 'source_point', 'dest_point']
    )
  }}

)

SELECT *

FROM calculate_distance
