SELECT
    *
FROM
    {{ ref('agg_per_user') }}
WHERE
    average_time_per_program < 0