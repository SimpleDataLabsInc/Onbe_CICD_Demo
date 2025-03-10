{% test count_records(model) %}
with actual_count AS (
  select
    '{{ model }}' AS model,
    count(*) AS n_records
  from
    {{ model }}
)
SELECT
  model,
  n_records
FROM
  actual_count
WHERE
  ( model, n_records) NOT IN (
    ('customers', 100),
    ( 'orders', 99))
{% endtest %}

 