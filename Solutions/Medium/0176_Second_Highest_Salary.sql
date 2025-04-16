/*
#176: Second Highest Salary

Difficulty:
Medium

Problem:

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null.

*/

-- Solution
SELECT 
    MAX(salary) AS SecondHighestSalary
FROM 
    Employee
WHERE 
    salary < (SELECT MAX(salary) FROM Employee); -- Subquery to exclude highest salary

/*
Explanation:

1. Find the highest salary in the table.
2. Filter out the top salary, leaving only salaries that are less than the max.
3. Now get the next highest value (the second highest).

*/