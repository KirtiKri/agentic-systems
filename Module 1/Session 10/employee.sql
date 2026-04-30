-- Step 1 — Build the database

CREATE TABLE employees(

EmployeeID INT PRIMARY KEY,

Name VARCHAR(50),

Department VARCHAR(30),

Salary INT,

City VARCHAR(30),

JoiningDate INT

);

INSERT INTO employees VALUES (101, 'Aarav', 'Sales',    40000, 'Delhi',  2020);

INSERT INTO employees VALUES (102, 'Diya',  'HR',     55000, 'Mumbai',  2019);

INSERT INTO employees VALUES (103, 'Kabir', 'Sales',    60000, 'Delhi',  2021);

INSERT INTO employees VALUES (104, 'Meera', 'IT',     75000, 'Bengaluru',2018);

INSERT INTO employees VALUES (105, 'Rohan', 'IT',     90000, 'Bengaluru',2017);

INSERT INTO employees VALUES (106, 'Sneha', 'HR',     50000, 'Mumbai',  2022);

INSERT INTO employees VALUES (107, 'Vihaan', 'Finance',   70000, 'Delhi',  2019);

INSERT INTO employees VALUES (108, 'Ishaan', 'Finance',   85000, 'Mumbai',  2016);

INSERT INTO employees VALUES (109, 'Anaya', 'Sales',    45000, 'Bengaluru',2023);

INSERT INTO employees VALUES (110, 'Riya',  'IT',     95000, 'Delhi',  2015);



-- Step 2 — Answer the business questions

-- Query 1 

USE employee;

SELECT Name, Department, Salary 

FROM employees 

WHERE Salary >= 60000 

ORDER BY Salary DESC;



-- Query 2

SELECT DISTINCT Department FROM employees;



-- Query 3

SELECT Name, City, JoiningDate FROM employees

WHERE City IN ('Delhi', 'Mumbai')

AND JoiningDate < 2021;



-- Query 4

SELECT Name, Department, Salary FROM employees

ORDER BY Salary DESC

LIMIT 3;



-- Query 5

SELECT Name, Department FROM employees

WHERE Name LIKE 'R%';