with session_count as (
    select count(*) as freq 
    from {{ ref('session') }}
)
  
select * from session_count where freq = 0