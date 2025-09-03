{%- macro SpatialInfo_03(table_name, schema, geometryColumnName, geometryType, centroid) -%}
  {{ log("table_name=" ~ table_name, info=True) }}
  {{ log("schema=" ~ schema, info=True) }}
  {{ log("geometryColumnName=" ~ geometryColumnName, info=True) }}
  {{ log("geometryType=" ~ geometryType, info=True) }}
  {{ log("centroid=" ~ centroid, info=True) }}

  {%- if geometryType == 'LineString' -%}

  SELECT
    round(ST_Length(ST_GeogFromText({{geometry}})),0) as length,
    ST_AsText(ST_Centroid(ST_GeomFromText({{geometry}}))) as centroid,
    ST_AsText(ST_EndPoint(ST_GeomFromText({{geometry}}))) as endpoint,
    ST_AsText(ST_Envelope(ST_GeomFromText({{geometry}}))) as bounding_box,
    ST_NumGeometries(ST_GeomFromText({{geometry}})) as num_geometries,
    {{geometry}} as input
  FROM
    {{table_name}}

  {%- else -%}

  SELECT
    round(ST_Area(ST_GeogFromText({{geometryColumnName}}))/1000000,0) as area_kms,
    round(ST_Area(ST_GeogFromText({{geometryColumnName}}))/1000000/2.59,0) as area_miles,
    ST_AsText(ST_Centroid(ST_GeomFromText({{geometryColumnName}}))) as centroid,
    ST_Length(ST_GeomFromText({{geometryColumnName}})) as length,
    round(ST_Perimeter(ST_GeomFromText({{geometryColumnName}})), 2) as perimeter,
    ST_AsText(ST_Envelope(ST_GeomFromText({{geometryColumnName}}))) as bounding_box,
    ST_NumGeometries(ST_GeomFromText({{geometryColumnName}})) as num_geometries,
    {{geometryColumnName}}
  FROM
    {{table_name}}

  {%- endif -%}

{%- endmacro -%}