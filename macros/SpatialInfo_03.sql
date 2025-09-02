{%- macro SpatialInfo_03(table_name, schema, polygonColumnName, centroid) -%}
  {{ log("table_name=" ~ table_name, info=True) }}
  {{ log("schema=" ~ schema, info=True) }}
  {{ log("polygonColumnName=" ~ polygonColumnName, info=True) }}
  {{ log("centroid=" ~ centroid, info=True) }}

  SELECT
    round(ST_Area(ST_GeomFromText({{polygonColumnName}})),4) as area,
    ST_AsText(ST_Centroid(ST_GeomFromText({{polygonColumnName}}))) as centroid,
    ST_Length(ST_GeomFromText({{polygonColumnName}})) as length,
    round(ST_Perimeter(ST_GeomFromText({{polygonColumnName}})), 2) as perimeter,
    ST_AsText(ST_Envelope(ST_GeomFromText({{polygonColumnName}}))) as bounding_box,
    ST_NumGeometries(ST_GeomFromText({{polygonColumnName}})) as num_geometries,
    {{polygonColumnName}}
  FROM
    {{table_name}}

{%- endmacro -%}