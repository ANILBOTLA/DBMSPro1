The database name is bussinessmanagementsystem.
There are 4 tables, worker, profile, duty and company tables.
id is the primary key in worker table.
profile_id is the foreign key with id of profile table.
duty_id is the foreign key with id of duty table.
company_id is the foreign key with id of company table.
id is the primary key in profile table
id is the primary key in duty table
id is the primary key in company table.

profile_id, duty_id and organization_id is for the 3NF database.
for example:
1, 2 rows in worker table are different with id but profile_id is same,
So we can get id of profile and get all data from profile table