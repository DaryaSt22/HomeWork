CREATE TABLE Employeess
(
Id SERIAL PRIMARY KEY,
Name VARCHAR (100),
Position VARCHAR (100),
Department VARCHAR (100),
Salary INTEGER
);

INSERT INTO Employeess (Name, Position, Department, Salary)
VALUES
    ('John Doe', 'Manager', 'Sales', 4900),
    ('Jane Smith', 'Developer', 'IT', 60000);
    ('Vanya Ivanov', 'Advertising director', 'Marketing', 72000);

UPDATE Employeess
SET Position = 'Project manager'
WHERE name = 'Jane Smith';

ALTER TABLE Employeess
ADD COLUMN HireDate DATE;

UPDATE Employeess
SET HireDate = '2020-05-15'
WHERE NAME = 'John Doe';

UPDATE Employeess
SET HireDate = '2021-02-14'
WHERE NAME = 'Jane Smith';

UPDATE Employeess
SET HireDate = '2018-11-04'
WHERE NAME = 'Vanya Ivanov';

SELECT * FROM Employeess;

SELECT * FROM Employeess
WHERE salary > 5000;

SELECT * FROM Employeess
WHERE department = 'Sales';

SELECT AVG (salary) AS av_salary
FROM Employees;

DELETE FROM Employeess;
