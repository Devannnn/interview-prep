Here are two tables:

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

departments
+----+-------------+
| id | name        |
+----+-------------+
| 1  | Engineering |
| 2  | Marketing   |
| 3  | HR          |
+----+-------------+

Write a query that returns each department name alongside:
- the number of employees in it
- the average salary
- but only for departments with more than 2 employees

Expected output:
+-------------+-------+------------+
| dep_name    | count | avg_salary |
+-------------+-------+------------+
| Engineering | 3     | 88333.33   |
+-------------+-------+------------+


Answer:
SELECT d.name as dep_name, count(*) as count, avg(e.salary) as avg_salary
FROM employees as e
JOIN departments as d ON e.dep_id = d.id
GROUP BY d.name
HAVING count(*) > 2
