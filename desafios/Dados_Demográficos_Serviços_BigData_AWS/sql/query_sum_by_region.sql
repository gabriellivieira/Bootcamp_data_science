-- Por região

select region,
	sum(population)
from "populationDBAula"."population"
where region='Sul'
group by region;

-- Por estado

select state,
	sum(population)
from "populationDBAula"."population"
where state='Sao Paulo'
group by state;