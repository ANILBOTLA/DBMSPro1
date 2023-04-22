select * from worker
select * from profile
select * from duty
select * from company
insert into worker (profile_id, duty_id, company_id, code, status) values (2,3,4,'New',9)
insert into profile (firstName, lastName, intro, profile) values ("Gnan", "Bhai", "This is Gnan Bhai", "Wrestler")
insert into duty (title, slug, description) values ("Aded", "man", "This is new data")
insert into company (title, summary, status) values ("G Company", "This is G Company", 9)
delete from worker where code='Added'
delete from profile where lastName='Botla'
delete from duty where description='This is new record'
delete from company where title='G Company'
update profile set firstName='Anil' where firstName='Botla'