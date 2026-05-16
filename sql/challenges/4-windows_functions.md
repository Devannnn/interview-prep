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

Write a query that returns, for each employee, their name, salary, and their rank within their department by salary (highest = rank 1). Only return employees ranked 1 or 2 in their department.

Expected output:
+----------+--------+------+
| name     | salary | rank |
+----------+--------+------+
| Charlie  | 95000  | 1    |
| Alice    | 90000  | 2    |
| Diana    | 70000  | 1    |
| Bob      | 60000  | 2    |
+----------+--------+------+

Answer:
SELECT 
    name, 
    salary, 
    rank
FROM (SELECT 
        name, 
        salary, 
        RANK() OVER (PARTITION BY dep_id ORDER BY salary DESC) as rank
    FROM employees) as ranked
WHERE rank <= 2


Alternative:
WITH ranked AS (
    SELECT
        name,
        salary,
        RANK() OVER (PARTITION BY dep_id ORDER BY salary DESC) AS rank
    FROM employees
)
SELECT name, salary, rank
FROM ranked
WHERE rank <= 2