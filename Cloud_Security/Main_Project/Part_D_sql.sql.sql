/* (Database Fundamentals, Assignment Part D, Spring  2024 */

/* First author's name: Ran Vyvyan (Student ID 25465550) */
/* First author's email: ran.vyvyan@student.uts.edu.au */

/* Second author's name: Christopher Luu (Student ID 25556693)*/
/* Second author's email: christopher.luu@student.uts.edu.au */

/* Third author's name: Abdulaziz Almehmadi 14510630 (Student ID 14510630)*/
/* Third author's email: abdulaziz.s.almehmadi@student.uts.edu.au */


/* script name: YourdbName.SQL */
/* purpose:     Builds PostgreSQL tables for Apple App store database */
/* date:        27 October 2024 */
/* The URL for the website related to this database is https://www.apple.com/au/apps/ */

--=================================================================================================
-- Drop the tables below
DROP TABLE IF EXISTS User_T;
DROP TABLE IF EXISTS App_T;
DROP TABLE IF EXISTS Download_T;

--=================================================================================================
-- Create and insert into the tables below
CREATE TABLE User_T
    (AppleID       VARCHAR(32) NOT NULL,
     UserFName      VARCHAR(50) NOT NULL,      
     UserLName      VARCHAR(50) NOT NULL,
     DOB            DATE        NOT NULL,
     PhoneNumber    NUMERIC(10), 
     PassWord       VARCHAR(15) NOT NULL,
CONSTRAINT User_PK PRIMARY KEY (AppleID));

CREATE TABLE App_T
    (AppID        int NOT NULL,
     Name           VARCHAR(50) NOT NULL,
     Description    VARCHAR(250) NOT NULL,
     ReleaseDate    Date NOT NULL,
     AvailableLanguage VARCHAR(20) NOT NULL,
     SizeinMb       DECIMAL (10, 1),
     AgeRating      VARCHAR (4),
     Compatibility  VARCHAR (100),
CONSTRAINT App_PK PRIMARY KEY (AppID));

CREATE TABLE Download_T
    (AppleID       VARCHAR(32) NOT NULL,
     AppID         int NOT NULL,
     DateOfDownload Date,
CONSTRAINT Download_PK PRIMARY KEY (AppleID, AppID),
CONSTRAINT Download_FK1 FOREIGN KEY (AppleID) References User_T(AppleID),
CONSTRAINT Download_FK2 FOREIGN KEY (AppID) References App_T(AppID));


Insert into User_T values
('jennychen@gmail.com', 'Jenny', 'Chen', '01/01/1999', '0514636861', 'xd12G@g'),
('christianyu@gmail.com', 'Christian', 'Yu', '06/09/1990', '0413252572', 'DPRIAN90'),
('bibi@gmail.com', 'Bibi', 'Kim', '12/12/2004', '0345879357', 'Coco@xx'),
('sabrinacarpenter@gmail.com', 'Sabrina', 'Carpenter', '07/15/2005', '0478357146', 'nonsencebyme'),
('jimmybrown@gmail.com', 'Jimmy', 'Brown', '02/19/2000', '0416380909', 'Rghy@dhjkd'),
('jenorjenny@gmail.com', 'Jenny', 'Martin', '11/11/2002', '0635168460', 'fthtjszwju');

Insert into App_T values
('1235', 'Netflix', 'Netflix is a subscription-based streaming service that allows 
our members to watch TV shows and movies on an internet-connected device.', '08/26/2010', 'English', '168.6', '12+', 
'iOS 17.0'),
('2110', 'Discord', 'Discord is a voice, video, and text chat app that is used
by tens of millions of people ages 13+ to talk and hang out with their communities and friends.', '05/13/2015', 'English', 
'214.3', '17+', 'iOS 14.0'),
('5683', 'Uber', 'Uber is an app that connects drivers with riders. It is as simple as that.', '05/20/2010', 'English', 
'491.4', '4+', 'iOS 16.2'),
('4200', 'PAC-MAN', 'Play PAC-MAN, the retro arcade game you know and love! Featuring new modes, mazes, power-ups, 
and more! Join millions of fans eating PAC-DOTS and chomping GHOSTS in this exciting arcade classic, 
updated for mobile!', '06/01/2015', 'English', '255.4', '4+', 'iOS 12.0'),
('9480', 'Disney+', 'Disney+ is the streaming home of your favourite stories from Disney, Pixar, Marvel, Star Wars, 
National Geographic and Star.', '11/12/2019', 'English', '166.9', '4+', 'iOS 16.0'),
('674', 'Instagram', 'Instagram is a social media platform and photo-sharing app where users can upload, 
edit, and share photos and videos.', '10/06/2010', 'English', '347.2', '12+', 'iOS 15.1');


Insert into Download_T values
('jennychen@gmail.com', '5683', '10/15/2016'),
('christianyu@gmail.com', '4200', '10/21/2024'),
('christianyu@gmail.com', '9480', '12/01/2029'),
('bibi@gmail.com', '2110', '07/24/2019'),
('sabrinacarpenter@gmail.com', '2110', '11/03/2023'),
('jimmybrown@gmail.com', '2110', '03/18/2020'),
('jimmybrown@gmail.com', '674', '01/06/2012'),
('jenorjenny@gmail.com', '2110', '09/27/2022');





--=================================================================================================
-- Select * from TableName Statements
-- Note: Please write the “select * from TableName” statements in one line.

-- 2.b.1: Question: Get all the information of User in the database  
-- 2.b.1: SELECT statement: 
Select * from User_T;

-- 2.b.2: Question: Get all the information of App in the database 
-- 2.b.2: SELECT statement:
Select * from App_T;

-- 2.b.3: Question: Get all the information of Download in the database
-- 2.b.3: SELECT statement:
Select * from Download_T;

--=================================================================================================
-- 3.a: Question: Get the average size of apps for each AgeRating
-- 3.a: SELECT statement uinsg Group by:
Select round(avg(sizeinMb)) as AverageSizeofApp,AgeRating from App_T
Group by AgeRating;


-- 3.b: Question: Get the information of all users who installed any apps, where the user's name is 'Jenny'.
-- 3.b: SELECT statement uisng Inner Join:
Select *
from User_T UT inner join Download_T DT
on UT.AppleID = DT.AppleID 
where UserFName = 'Jenny';


-- 3.c: Question: Get the names and release date of the app has the smallest AppID
-- 3.c: SELECT statement using Sub Query:
Select Name, ReleaseDate
from App_T
where AppID = (Select min(AppID)
from App_T);



