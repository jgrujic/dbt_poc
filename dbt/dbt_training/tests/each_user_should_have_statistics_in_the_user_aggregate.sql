select *
from {{ ref('enriched_session') }} es
         left join {{ ref('agg_per_user') }} agg
                   on es.users = agg.users
where agg.users is NULL