create database sportslevelling;
use sportslevelling;
Create table Equipments(
Equipment varchar(225),
Number_of_equipments_available int);
insert into Equipments(Equipment , Number_of_equipments_available)
values('Basketball',1000),
	('Cricket Ball(leather)',10000),
    ('Cricket Helmet',2000),
    ('Batting Gloves',4000),
    ('Thigh pads',5000),
    ('Pads',4000),
    ('Stumps',6561),
    ('Bats',1000),
    ('Keeping Gloves',5000),
    ('Football',2000),
    ('Badminton Rackets',3000),
    ('Table Tennis Rackets',500),
    ('Lawn Tennis Rackets',300);
    select * from Equipments;
    
    