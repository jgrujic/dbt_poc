SELECT
    *
FROM
    {{ ref('agg_per_program') }}
WHERE
    unique_users_watched <= 0