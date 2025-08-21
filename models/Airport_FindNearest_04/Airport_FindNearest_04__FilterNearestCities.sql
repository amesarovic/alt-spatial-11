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

distribution_centers AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'distribution_centers') }}

),

Distribution_Centers AS (

  {{ DatabricksSqlSpatial.CreatePoint('distribution_centers', [['lon', 'lat', 'point']]) }}

),

FindNearest AS (

  {{
    DatabricksSqlSpatial.FindNearest(
      ['Distribution_Centers', 'US_Airports_1'], 
      'point', 
      'point', 
      'point', 
      'point', 
      200, 
      500, 
      'mls', 
      true, 
      ['city', 'name', 'lat', 'lon', 'point'], 
      ['city', 'state', 'lat', 'lon', 'iata_code', 'name', 'point']
    )
  }}

),

FilterNearestCities AS (

  SELECT * 
  
  FROM FindNearest AS in0
  
  WHERE distanceMiles > 100

)

SELECT *

FROM FilterNearestCities
