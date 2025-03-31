SELECT ROUND(RAND() * 10000, 2);
UPDATE Users u set Salary = ROUND(RAND() * 10000, 2);

SELECT Salary from Users u WHERE 
Salary between 1000 and 1500
order by salary asc;