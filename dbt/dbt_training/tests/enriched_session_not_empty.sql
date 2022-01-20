with session_count as (
    select count(*) as freq 
    from {{ ref('enriched_session') }}
)
  
select * from session_count where freq = 0