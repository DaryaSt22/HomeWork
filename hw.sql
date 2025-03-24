CREATE TABLE Employees
(
Id SERIAL PRIMARY KEY,
Name CHARACTER VARYING(30),
Position CHARACTER VARYING(30),
Department  CHARACTER VARYING(30),
Salary INTEGER

);

ALTER TABLE Employees ADD COLUMN HireDate DATE; 
INSERT INTO Employees (Name, Position, Department, Salary, HireDate)
VALUES 
('John Doe', 'Manager', 'Sales', 50000, 2011);

ALTER TABLE employees
ALTER COLUMN HireDate DROP NOT NULL;
