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
    ('ONBE_DEMO_DEV.PUBLIC.customers', 100),
    ('ONBE_DEMO_DEV.PUBLIC.orders', 99),
    ('ONBE_DEMO_PROD.PUBLIC.customers', 100),
    ('ONBE_DEMO_PROD.PUBLIC.orders', 99))
{% endtest %}

 