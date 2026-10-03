SHOW DATABASES;
USE NIT
SHOW TABLES;
SELECT * FROM STUDENT;
SELECT SUM(MARKS) FROM STUDENT;
SELECT COUNT(NAME) FROM STUDENT;
SELECT MAX(MARKS) FROM STUDENT;
SELECT * FROM STUDENT ORDER BY MARKS DESC;
SELECT * FROM STUDENT WHERE NAME LIKE 'Y%';
SELECT * FROM STUDENT WHERE NAME LIKE '%Y';
SELECT * FROM STUDENT WHERE NAME LIKE '_Y%';
SELECT * FROM STUDENT WHERE NAME LIKE '%A__';
UPDATE student VALUES 
('alex', 45, 'hyd', 79),
('cathy', 17, 'delhi', 90),
('dolly', 48, 'pune', 67),
('chancy', 78, 'mumbai', 34),
('ethan', 22, 'bangalore', 88),
('fiona', 31, 'chennai', 74),
('george', 55, 'kolkata', 62),
('hannah', 19, 'jaipur', 95),
('ian', 63, 'ahmedabad', 53),
('julia', 28, 'lucknow', 81),
('kevin', 40, 'hyd', 69),
('laura', 16, 'pune', 92),
('michael', 52, 'delhi', 45),
('nina', 35, 'mumbai', 78),
('oliver', 24, 'bangalore', 84),
('priya', 29, 'chennai', 89),
('quinn', 61, 'kolkata', 58),
('rahul', 18, 'jaipur', 76),
('sarah', 44, 'ahmedabad', 65),
('tom', 33, 'lucknow', 82),
('uma', 27, 'hyd', 71),
('victor', 50, 'delhi', 60),
('wendy', 21, 'pune', 94),
('xavier', 73, 'mumbai', 42),
('yash', 38, 'bangalore', 85),
('zara', 15, 'chennai', 99),
('aaron', 47, 'kolkata', 51),
('bella', 26, 'jaipur', 87),
('chris', 59, 'ahmedabad', 63),
('diana', 30, 'lucknow', 77),
('eric', 42, 'hyd', 68),
('fatima', 20, 'delhi', 91),
('gavin', 67, 'pune', 49),
('helen', 34, 'mumbai', 83),
('ishaan', 23, 'bangalore', 75),
('jenny', 58, 'chennai', 56),
('karan', 19, 'kolkata', 80),
('lily', 49, 'jaipur', 72),
('manish', 36, 'ahmedabad', 66),
('neha', 25, 'lucknow', 93),
('oscar', 64, 'hyd', 48),
('pooja', 32, 'delhi', 86),
('qasim', 46, 'pune', 59),
('rohit', 22, 'mumbai', 73),
('sneha', 39, 'bangalore', 89),
('tina', 54, 'chennai', 61),
('usman', 28, 'kolkata', 70),student
('valerie', 17, 'jaipur', 96),
('will', 51, 'ahmedabad', 54),
('zoe', 37, 'lucknow', 85);
SELECT * FROM STUDENT;

 