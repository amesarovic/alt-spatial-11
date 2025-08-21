{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH airports AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'us_airports_2') }}

),

customers AS (

  SELECT * 
  
  FROM {{ ref('customers')}}

),

customers_2 AS (

  {{ DatabricksSqlSpatial.CreatePoint('customers', [['lon', 'lat', 'point']]) }}

),

airports_2 AS (

  {{ DatabricksSqlSpatial.CreatePoint('airports', [['lon', 'lat', 'point']]) }}

),

FindNearest AS (

  {{
    DatabricksSqlSpatial.FindNearest(
      ['customers_2', 'airports_2'], 
      'point', 
      'point', 
      'point', 
      'point', 
      100, 
      200, 
      'mls', 
      false, 
      ['customer_id', 'city', 'name', 'lat', 'lon', 'point'], 
      ['city', 'state', 'lat', 'lon', 'iata_code', 'name', 'point']
    )
  }}

)

SELECT *

FROM FindNearest
