Here a table:

employees
+----+----------+--------+-------+
| id | name     | salary | dep_id|
+----+----------+--------+-------+
| 1  | Alice    | 90000  | 1     |
| 2  | Bob      | 60000  | 2     |
| 3  | Charlie  | 95000  | 1     |
| 4  | Diana    | 70000  | 2     |
| 5  | Eve      | 80000  | 1     |
+----+----------+--------+-------+

Write a query that returns the name and salary of all employees who earn more than the average salary across the whole company.

Expected output:
+----------+--------+
| name     | salary |
+----------+--------+
| Alice    | 90000  |
| Charlie  | 95000  |
+----------+--------+


Answer:
SELECT e.name, e.salary
FROM employees as e
WHERE e.salary > (SELECT avg(e2.salary) FROM employees as e2)
