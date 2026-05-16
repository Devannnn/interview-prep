# SQL — interview questions

## Table of contents

- [1. What's SQLite?](#1-whats-sqlite)
- [2. What are primary keys and foreign keys?](#2-what-are-primary-keys-and-foreign-keys)
- [3. What are database constraints?](#3-what-are-database-constraints)
- [4. What is the difference between INNER JOIN and LEFT JOIN?](#4-what-is-the-difference-between-inner-join-and-left-join)
- [5. What is the difference between WHERE and HAVING?](#5-what-is-the-difference-between-where-and-having)
- [6. What is the difference between GROUP BY and ORDER BY?](#6-what-is-the-difference-between-group-by-and-order-by)
- [7. What is a database migration?](#7-what-is-a-database-migration)
- [8. What's an ORM? Can you name one drawback or risk of using an ORM?](#8-whats-an-orm-can-you-name-one-drawback-or-risk-of-using-an-orm)
- [9. What is an SQL index and why is it useful?](#9-what-is-an-sql-index-and-why-is-it-useful)
- [10. What is a transaction?](#10-what-is-a-transaction)
- [11. What are ACID properties?](#11-what-are-acid-properties)
- [12. What is the N+1 query problem in an ORM?](#12-what-is-the-n1-query-problem-in-an-orm)
- [13. How do you implement efficient pagination in an API?](#13-how-do-you-implement-efficient-pagination-in-an-api)
- [14. Why use a search engine like Elasticsearch?](#14-why-use-a-search-engine-like-elasticsearch)

---

#### 1. What's SQLite?

<details>
<summary>Reveal answer</summary>

SQLite is a file-based relational database. It's convenient because unlike traditional database like MySQL, you don't need a separate server process nor installation.

That makes it the best choice if you need a fast way to persist data for local development.

However it lacks features needed in production like concurrent writing. That's why it's not recommended in production and is then replaced by a system like PostgreSQL.

</details>

---

#### 2. What are primary keys and foreign keys?

<details>
<summary>Reveal answer</summary>

A primary key is a column, or group of columns, that uniquely identifies a row in a table. It must be unique and cannot be NULL.

A foreign key is a column that references a row in another table, usually by storing that table's primary key. It is used to represent relationships between tables and helps ensure that the referenced row actually exists.

</details>

---

#### 3. What are database constraints?

<details>
<summary>Reveal answer</summary>

A database constraint is a rule enforced by the database to keep data valid and consistent. It can apply to columns, tables, or relationships.

For example, a column can be `NOT NULL`, `UNIQUE`, or a foreign key referencing another table. A table can have a constraint that says that a row is valid only if the `start_date` column is before the `end_date` column.

</details>

---

#### 4. What is the difference between INNER JOIN and LEFT JOIN?

<details>
<summary>Reveal answer</summary>

Those two keywords are used to match rows between two tables. The difference is how they match those rows.

INNER JOIN (or only JOIN) returns rows that match in both tables. For example, to get the list of users along with their favorite movie.

```sql
SELECT users.name, movies.title
FROM users
JOIN movies ON users.favorite_movie_id = movies.id;
```

The caveat here is that users with no favorite movie defined won't be returned.

In many cases, you would like them to be returned even with an empty value. That's what LEFT JOIN is for.

LEFT JOIN returns all rows from the left table, even if there is no matching row in the right table. When there is no match, the right-side column is NULL.

```sql
SELECT users.name, movies.title
FROM users
LEFT JOIN movies ON users.favorite_movie_id = movies.id;
```

RIGHT JOIN also exists but in practice, most teams mostly use LEFT JOIN and swap table order instead.

</details>

---

#### 5. What is the difference between WHERE and HAVING?

<details>
<summary>Reveal answer</summary>

`WHERE` and `HAVING` are both used to filter query results, but they apply at different stages.

`WHERE` filters rows before grouping.

`HAVING` filters groups after grouping.


```sql
SELECT user_id, COUNT(*) AS order_count
FROM orders
WHERE status = 'paid'
GROUP BY user_id
HAVING COUNT(*) >= 3;
```

</details>

---

#### 6. What is the difference between GROUP BY and ORDER BY?

<details>
<summary>Reveal answer</summary>

`GROUP BY` groups rows that have the same value in one or more columns. It is usually used with aggregate functions like `COUNT`, `SUM`, or `AVG`.

`ORDER BY` sorts the final result of a query. It can sort rows or grouped results, in ascending or descending order.

</details>

---

#### 7. What is a database migration?

<details>
<summary>Reveal answer</summary>

In backend development, a database migration usually means a controlled change to the database schema, such as creating a table, adding a column, changing a constraint, or adding an index.

More precisely, this is a schema migration. A migration can also include data changes, such as backfilling values for existing rows. The term database migration can also be used more broadly for moving data from one database system to another, like MySQL to PostgreSQL, but in application development it often refers to schema changes over time.

</details>

---

#### 8. What's an ORM? Can you name one drawback or risk of using an ORM?

<details>
<summary>Reveal answer</summary>

An Object Relational Mapper, or ORM, is an abstraction used in software development to let application code interact with a relational database using entities instead of raw SQL. The idea is to represent database concepts with OOP: tables become classes, columns become attributes, and rows become instances.

The main advantage of an ORM is that it's natural to manipulate classes and instances in a code, whereas manipulating raw SQL is error-prone and requires to know about specific SQL syntax.

With an ORM, the actual SQL requests are built under the hood. They're also optimized for security. For instance, ORMs have in-built SQL injection protections that a code using raw SQL might lack.

The main drawback is that it hides the generated SQL. The SQL may be inefficient (N+1 queries problem), and this extra abstraction layer can make performance problems or debugging harder.

</details>

---

#### 9. What is an SQL index and why is it useful?

<details>
<summary>Reveal answer</summary>

Index is a concept in SQL meant to make data retrieval much more performant.

The idea is that, when searching for an element, the database may need to scan many rows to find the target element. That's because rows were inserted without concerns for search time.

An index solves this issue. It's another representation of available data, sorted by one or more columns. For example, the list of books sorted by author.

The index is optimized for searching and each of its elements points to the actual rows it represents.

The trade-off is extra storage and slower writes, because the index must be updated when rows are inserted, updated, or deleted.
</details>

---

#### 10. What is a transaction?

<details>
<summary>Reveal answer</summary>

A transaction is a group of database operations performed together as one unit.

It is useful when several operations only make sense if they all succeed. If only part of them are applied, the database could be left in an inconsistent state. To prevent this, transactions allow the database to commit all the operations if they succeed, or roll them back if one operation fails.

</details>

---

#### 11. What are ACID properties?

<details>
<summary>Reveal answer</summary>

ACID describes four properties that make database transactions reliable.

`Atomicity` means a transaction is all-or-nothing: either all operations succeed, or none are applied.

`Consistency` means a transaction should move the database from one valid state to another, while respecting constraints and rules.

`Isolation` means concurrent transactions should not interfere with each other in unsafe ways.

`Durability` means that once a transaction is committed, the change should be persisted even if the system crashes afterward.


</details>

---

#### 12. What is the N+1 query problem in an ORM?

<details>
<summary>Reveal answer</summary>

The N+1 query problem is often used to describe performance issues with ORM. It happens when the ORM performs one query to get a list of elements, then performs an additional query per element, hence resulting in N+1 queries.

For example, if you have a table Car and a table Wheel with a one-to-many relationship between the two tables then an ORM might do SELECT * FROM Car and then SELECT * FROM Wheel where car.id = x.

Doing that many small queries is inefficient. It's often more efficient to do one complex query. That's because each round trips to the database is expensive.

Which means that you could get the same data in a much more efficient way if you were doing a more complex query such as a join.

</details>

---

#### 13. How do you implement efficient pagination in an API?

<details>
<summary>Reveal answer</summary>

A simple way to paginate is to use `LIMIT` and `OFFSET`. For example, with a page size of 50, the first query uses `LIMIT 50 OFFSET 0`, the second uses `LIMIT 50 OFFSET 50`, and so on.

```sql
SELECT *
FROM posts
ORDER BY id
LIMIT 50 OFFSET 10000;
```

This works well for simple cases, but it can become inefficient for large offsets because the database still has to go through the first X rows before reaching the offset, skip all of them, then returns the next rows.

A solution to this is cursor pagination. The idea is similar but instead of 'skipping' the first X rows, you start directly after the last element you've seen.

```sql
SELECT *
FROM posts
WHERE id > 10000
ORDER BY id
LIMIT 50;
```

</details>

---

#### 14. Why use a search engine like Elasticsearch?

<details>
<summary>Reveal answer</summary>

A search engine like Elasticsearch is useful when a relational database is not enough for advanced search features.

It is optimized for full-text search, relevance ranking, fuzzy search, typo tolerance, autocomplete, and filtering large sets of documents quickly.

In many applications, the relational database remains the source of truth, while Elasticsearch stores a searchable copy of the data.

</details>

