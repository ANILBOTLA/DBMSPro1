insert  into `worker`(`id`,`profile_id`,`duty_id`,`company_id`,`code`,`status`) values 
(1,1,1,1,'Software',1),
(2,1,2,3,'Teaching',2),
(3,3,5,2,'Research',5),
(4,6,3,4,'Mechanical',6),
(5,4,4,6,'Doctor',3),
(6,2,6,5,'Police',2),
(7,5,5,2,'Actor',4);

insert  into `company`(`id`,`title`,`summary`,`status`) values 
(1,'X Company','This is X Company',1),
(2,'Y Company','This is y Company',2),
(3,'Z Company','This is z Company',3),
(4,'P Company','This is P Company',4),
(5,'Q Company','This is Q Company',5),
(6,'R Company','This is R Company',6);

insert  into `duty`(`id`,`title`,`slug`,`description`) values 
(1,'Owner','own','This is Owner'),
(2,'Contractor','Contract','This is Contractor'),
(3,'ChairPerson','Chair','This is ChairPerson'),
(4,'Head Of Dept','Head Of Dept','This is Head Of Dept'),
(5,'Architect','Architect','This is Architect'),
(6,'Lead','Lead','This is Lead');

insert  into `profile`(`id`,`firstName`,`lastName`,`intro`,`profile`) values 
(1,'Virat','kohli','This is Virat kohli','Hard working batsman'),
(2,'Rohit','Sharma','This is Rohit Sharma','Lucky captain'),
(3,'MS','Dhoni','This is MS Dhoni','Wicket keeper'),
(4,'Rahul','Dravid','This is Rahul Dravid','The Wall'),
(5,'Joe','Root','This is Joe Root','TestBatsman'),
(6,'Adam','Zampa','This is Adam Zampa','Spinner');