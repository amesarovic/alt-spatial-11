{%- macro SpatialInfo_03(table_name, schema, geometryColumnName, geometryType, centroid) -%}
  {{ log("table_name=" ~ table_name, info=True) }}
  {{ log("schema=" ~ schema, info=True) }}
  {{ log("geometryColumnName=" ~ geometryColumnName, info=True) }}
  {{ log("geometryType=" ~ geometryType, info=True) }}
  {{ log("centroid=" ~ centroid, info=True) }}

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

{%- endmacro -%}