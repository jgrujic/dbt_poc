select *
from {{ ref('session') }} s
where beginning > finish