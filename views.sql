create view total as
select Date(time) as day , count(*) as visits
from log group by day order by day;


create view total_error as
select date(time) as day , count(*) as errors
from log where status='404 NOT FOUND' group by day order by day;

create view error_percentage as
select total.day , round(100.000 * erqrors / visits , 3 ) as perc
from total join total_error
on total.day = total_error.day;

