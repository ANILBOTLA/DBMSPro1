select * from worker
select * from profile
select * from duty
select * from company
insert into worker (profile_id, duty_id, company_id, code, status) values (2, 3, 4, 'Another', 8)
insert into profile (firstName, lastName, intro, profile) values ("Mary", "Crown", "This is Mary Crown", "Graduate")
insert into duty (title, slug, description) values ("Manager", "man", "This is another manager")
insert into company (title, summary, status) values ("G Company", "This is G Company", 9)
delete from worker where code='Another'
delete from profile where lastName='Crown'
delete from duty where description='This is another manager'
delete from company where title='G Company
update profile set firstName='Oxen' where firstName='James'