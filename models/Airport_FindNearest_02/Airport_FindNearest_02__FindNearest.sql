{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_airports AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'us_airports_50k') }}

),

US_Airports_1 AS (

  {{ DatabricksSqlSpatial.CreatePoint('us_airports', [['lon', 'lat', 'point']]) }}

),

customers AS (

  SELECT * 
  
  FROM {{ ref('customers')}}

),

Customers_1 AS (

  {{ DatabricksSqlSpatial.CreatePoint('customers', [['lon', 'lat', 'point']]) }}

),

FindNearest AS (

  {{
    DatabricksSqlSpatial.FindNearest(
      ['Customers_1', 'US_Airports_1'], 
      'point', 
      'point', 
      'point', 
      'point', 
      50, 
      500, 
      'kms', 
      false, 
      ['customer_id', 'city', 'name', 'lat', 'lon', 'point'], 
      ['city', 'state', 'lat', 'lon', 'iata_code', 'name', 'point']
    )
  }}

)

SELECT *

FROM FindNearest
