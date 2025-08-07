{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH points AS (

  SELECT * 
  
  FROM {{ ref('points')}}

),

create_geo_point AS (

  {{ DatabricksSqlSpatial.CreatePoint('points', [['lon', 'lat', 'point']]) }}

)

SELECT *

FROM create_geo_point
