CREATE TABLE student(
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email VARCHAR(60) NULL,
street VARCHAR(50) NOT NULL,
city VARCHAR(40) NOT NULL,
state VARCHAR(2) NOT NULL DEFAULT "PA",
zip MEDIUMINT UNSIGNED NOT NULL,
phone VARCHAR(20) NOT NULL,
birth_date DATE NOT NULL,
sex ENUM('M', 'F') NOT NULL,
date_entered TIMESTAMP,
lunch_cost FLOAT NULL,
student_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE class(
name VARCHAR(30) NOT NULL,
class_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY);

CREATE TABLE test(
date DATE NOT NULL,
type ENUM('T', 'Q') NOT NULL,
class_id INT UNSIGNED NOT NULL,
test_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY);

CREATE TABLE score(
student_id INT UNSIGNED NOT NULL,
event_id INT UNSIGNED NOT NULL,
score INT NOT NULL,
PRIMARY KEY(event_id, student_id));

CREATE TABLE absence(
student_id INT UNSIGNED NOT NULL,
date DATE NOT NULL,
PRIMARY KEY(student_id, date));


-- Inputting maxscore into test table
ALTER TABLE test ADD maxscore INT NOT NULL AFTER type;

-- changing event_id to test_id
ALTER TABLE score CHANGE event_id test_id
	INT UNSIGNED NOT NULL;

-- Renaming all tables names
RENAME TABLE
	absence to absences,
	class to classes,
	score to scores,
	student to students,
	test to tests;
