{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH JSONParse_1 AS (

  {{ DatabricksSqlBasics.JSONParse('', '', 'parseFromSampleRecord', '', '') }}

)

SELECT *

FROM JSONParse_1
