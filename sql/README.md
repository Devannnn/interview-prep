# SQL — interview questions

## Table of contents

- [1. What is the difference between INNER JOIN and LEFT JOIN?](#1-what-is-the-difference-between-inner-join-and-left-join)
- [2. What is an SQL index and why is it useful?](#2-what-is-an-sql-index-and-why-is-it-useful)
- [3. How do you implement efficient pagination in an API?](#3-how-do-you-implement-efficient-pagination-in-an-api)
- [4. How do you handle a database that becomes very large?](#4-how-do-you-handle-a-database-that-becomes-very-large)
- [5. Why use a search engine like Elasticsearch?](#5-why-use-a-search-engine-like-elasticsearch)
- [6. What is the difference between a relational database and a search engine?](#6-what-is-the-difference-between-a-relational-database-and-a-search-engine)
- [7. How does search indexing work in Elasticsearch?](#7-how-does-search-indexing-work-in-elasticsearch)
- [8. What is the difference between WHERE and HAVING?](#8-what-is-the-difference-between-where-and-having)
- [9. What is the difference between GROUP BY and ORDER BY?](#9-what-is-the-difference-between-group-by-and-order-by)
- [10. What are primary keys and foreign keys?](#10-what-are-primary-keys-and-foreign-keys)
- [11. What are database constraints?](#11-what-are-database-constraints)
- [12. What is normalization? When would you denormalize?](#12-what-is-normalization-when-would-you-denormalize)
- [13. What is a transaction?](#13-what-is-a-transaction)
- [14. What are ACID properties?](#14-what-are-acid-properties)
- [15. What is a database migration?](#15-what-is-a-database-migration)
- [16. What's SQLite ?](#16-whats-sqlite)
- [17. What's an ORM ? Can you name one drawback or risk of using an ORM?](#17-whats-an-orm-can-you-name-one-drawback-or-risk-of-using-an-orm)
- [18. What is the N+1 query problem in an ORM?](#18-what-is-the-n1-query-problem-in-an-orm)

---

#### 1. What is the difference between INNER JOIN and LEFT JOIN?

<details>
<summary>Reveal answer</summary>

Those two keywords are used to match rows between two tables. The difference is how they match those rows.

INNER JOIN (on only JOIN) returns rows that match in both tables. For example, to get the list of users along with their favorite movie.

```sql
SELECT [users.name](http://users.name/), movies.title
FROM users
JOIN movies ON users.favorite_movie_id = [movies.id](http://movies.id/);
```

The caveat here is that users with no favorite movie defined won't be returned.

In many cases, you would like them to be returned even with an empty value. That's what LEFT join is for.

LEFT JOIN returns all rows from the left table, even if there is no matching row in the right table. When there is no match, the right-side column is NULL.

```sql
SELECT [users.name](http://users.name/), movies.title
FROM users
LEFT JOIN movies ON users.favorite_movie_id = [movies.id](http://movies.id/);
```

RIGHT JOIN also exists but in practice, most teams mostly use LEFT JOIN and swap table order instead.

</details>

---

#### 2. What is an SQL index and why is it useful?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 3. How do you implement efficient pagination in an API?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 4. How do you handle a database that becomes very large?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 5. Why use a search engine like Elasticsearch?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 6. What is the difference between a relational database and a search engine?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 7. How does search indexing work in Elasticsearch?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 8. What is the difference between WHERE and HAVING?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 9. What is the difference between GROUP BY and ORDER BY?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 10. What are primary keys and foreign keys?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 11. What are database constraints?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 12. What is normalization? When would you denormalize?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 13. What is a transaction?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 14. What are ACID properties?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 15. What is a database migration?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 16. What's SQLite ?

<details>
<summary>Reveal answer</summary>

SQLite is a file-based relational database. It's convenient because unlike traditional database like MySQL, you don't need a separate server process nor installation.

That makes it the best choice if you need a fast way to persist data for local development.

However it lacks features needed in production like concurrent writing. That's why it's not recommended in production and is then replaced by a system like PostgreSQL.

</details>

---

#### 17. What's an ORM ? Can you name one drawback or risk of using an ORM?

<details>
<summary>Reveal answer</summary>

An Object Relational Mapper, or ORM, is an abstraction used in software development to let application code interact with a relational database using entities instead of raw SQL. The idea is to represent database concepts with OOP: tables become classes, columns become attributes, and rows become instances.

The main advantage of an ORM is that it's natural to manipulate classes and instances in a code, whereas manipulating raw SQL is error-prone and requires to know about specific SQL syntax.

With an ORM, the actual SQL requests are built under the hood. They're also optimized for security. For instance, ORMs have in-built SQL injection protections that a code using raw SQL might lack.

The main drawback is that it hides the generated SQL. The SQL may be inefficient (N+1 queries problem), and this extra abstraction layer can make performance problems or debugging harder.s

</details>

---

#### 18. What is the N+1 query problem in an ORM?

<details>
<summary>Reveal answer</summary>

The N+1 query problem is often used to describe performance issues with ORM. It happens when the ORM performs one query to get a list of elements, then performs an additional query per element, hence resulting in N+1 queries.

For example, if you have a table Car and a table Wheel with a one-to-many relationship between the two tables then an ORM might do SELECT * FROM Car and then SELECT * FROM Wheel where [car.id](http://car.id/) = x.

Doing that many small queries is inefficient. It's often more efficient to do one complex query. That's because each round trips to the database is expensive.

Which means that you could get the same data in a much more efficient way if you were doing a more complex query such as a join.

</details>

---
