{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH find_nearest_1 AS (

  SELECT * 
  
  FROM {{ ref('find_nearest_1')}}

),

find_nearest_2 AS (

  SELECT * 
  
  FROM {{ ref('find_nearest_2')}}

),

find_nearest_customers AS (

  {{
    DatabricksSqlSpatial.FindNearest(
      ['find_nearest_1', 'find_nearest_2'], 
      'customer_id', 
      'center_point', 
      'point', 
      'point', 
      1, 
      20, 
      'kms', 
      false, 
      ['customer_id', 'customer_point'], 
      ['center_id', 'center_point']
    )
  }}

)

SELECT *

FROM find_nearest_customers
