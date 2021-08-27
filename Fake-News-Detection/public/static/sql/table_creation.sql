drop table training_data

create table training_data (
	index bigint,
	URLs text,
	Headline text,
	Body text,
	Label bigint
)

select * from training_data