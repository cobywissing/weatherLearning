drop database weather; 
create database weather;
use weather;
create table main(EventId int not null Auto_Increment, Type varchar(15), Severity varchar(10), AirportCode varchar(10), month int(2), day int(2), year int, primary key (Eventid)) ENGINE=InnoDB;
create table isWeather(EventId int not null Auto_Increment, weather int, AirportCode varchar(10), month int(2), day int(2), year int, primary key (Eventid)) ENGINE=InnoDB;
create table duplicates(EventId int not null Auto_Increment, primary key (Eventid)) ENGINE=InnoDB;
create table duplicates2(EventId int not null Auto_Increment, primary key (Eventid)) ENGINE=InnoDB;
create table alldates(month int, day int, year int, primary key (month, day, year)) ENGINE=InnoDB;