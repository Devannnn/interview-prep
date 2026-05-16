Here are two tables:

employees                        departments
+----+----------+-------+        +----+-------------+
| id | name     | dep_id|        | id | name        |
+----+----------+-------+        +----+-------------+
| 1  | Alice    | 1     |        | 1  | Engineering |
| 2  | Bob      | 2     |        | 2  | Marketing   |
| 3  | Charlie  | 1     |        | 3  | HR          |
| 4  | Diana    | NULL  |        +----+-------------+
+----+----------+-------+

Write a query that returns the name of each employee alongside their department name. Employees without a department should still appear, showing NULL for the department.


Expected output:
+----------+-------------+
| name     | dep_name    |
+----------+-------------+
| Alice    | Engineering |
| Bob      | Marketing   |
| Charlie  | Engineering |
| Diana    | NULL        |
+----------+-------------+

Answer:
SELECT e.name as name, d.name as dep_name
FROM employees as e
LEFT JOIN departments as d ON e.dep_id = d.id