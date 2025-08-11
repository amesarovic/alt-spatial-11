{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH spatial_match_raw_20_fact AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_raw_20_fact')}}

),

Limit_1 AS (

  SELECT * 
  
  FROM spatial_match_raw_20_fact AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
