/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.6.7-MariaDB : Database - bussinessmanagementsystem
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bussinessmanagementsystem` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;

USE `bussinessmanagementsystem`;

/*Table structure for table `worker` */

DROP TABLE IF EXISTS `worker`;

CREATE TABLE `worker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) DEFAULT NULL,
  `duty_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `code` varchar(30) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `profile_id` (`profile_id`),
  KEY `duty_id` (`duty_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `company_id` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`),
  CONSTRAINT `duty_id` FOREIGN KEY (`duty_id`) REFERENCES `duty` (`id`),
  CONSTRAINT `profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

/*Data for the table `worker` */

insert  into `worker`(`id`,`profile_id`,`duty_id`,`company_id`,`code`,`status`) values 
(1,1,1,1,'Software',1),
(2,1,2,3,'Teaching',2),
(3,3,5,2,'Research',5),
(4,6,3,4,'Mechanical',6),
(5,4,4,6,'Doctor',3),
(6,2,6,5,'Police',2),
(7,5,5,2,'Actor',4);


/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(75) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

/*Data for the table `company` */

insert  into `company`(`id`,`title`,`summary`,`status`) values 
(1,'X Company','This is X Company',1),
(2,'Y Company','This is y Company',2),
(3,'Z Company','This is z Company',3),
(4,'P Company','This is P Company',4),
(5,'Q Company','This is Q Company',5),
(6,'R Company','This is R Company',6);

/*Table structure for table `duty` */

DROP TABLE IF EXISTS `duty`;

CREATE TABLE `duty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(75) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

/*Data for the table `duty` */

insert  into `duty`(`id`,`title`,`slug`,`description`) values 
(1,'Owner','own','This is Owner'),
(2,'Contractor','Contract','This is Contractor'),
(3,'ChairPerson','Chair','This is ChairPerson'),
(4,'Head Of Dept','Head Of Dept','This is Head Of Dept'),
(5,'Architect','Architect','This is Architect'),
(6,'Lead','Lead','This is Lead');

/*Table structure for table `profile` */

DROP TABLE IF EXISTS `profile`;

CREATE TABLE `profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(20) DEFAULT NULL,
  `lastName` varchar(20) DEFAULT NULL,
  `intro` varchar(255) DEFAULT NULL,
  `profile` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

/*Data for the table `profile` */

insert  into `profile`(`id`,`firstName`,`lastName`,`intro`,`profile`) values 
(1,'Virat','kohli','This is Virat kohli','Hard working batsman'),
(2,'Rohit','Sharma','This is Rohit Sharma','Lucky captain'),
(3,'MS','Dhoni','This is MS Dhoni','Wicket keeper'),
(4,'Rahul','Dravid','This is Rahul Dravid','The Wall'),
(5,'Joe','Root','This is Joe Root','TestBatsman'),
(6,'Adam','Zampa','This is Adam Zampa','Spinner');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
