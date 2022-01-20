select *
from {{ ref('session') }} s
         left join {{ ref('enriched_session') }} es
                   on s.channel = es.common_channel
                       and s.users = es.users
                       and es.beginning >= s.beginning and es.finish <= s.finish
where es.users is NULL