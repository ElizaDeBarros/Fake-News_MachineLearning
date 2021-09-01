drop table training_data

create table training_data (
	index bigint,
	URLs text,
	Headline text,
	Body text,
	Label bigint
)

select * from training_data

drop table prediction_data

create table prediction_data (
	index bigint,
	Body text,
	Logistic_Regression text,
	Naive_Bayes text,
	Decision_Tree text,
	Passive_Aggressive_Classifier text
)

select * from prediction_data