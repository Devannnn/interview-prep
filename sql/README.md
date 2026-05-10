# SQL — interview questions

## Table of contents

- [1. What is the difference between INNER JOIN and LEFT JOIN?](#1-what-is-the-difference-between-inner-join-and-left-join)
- [2. What is an SQL index and why is it useful?](#2-what-is-an-sql-index-and-why-is-it-useful)
- [3. How do you implement efficient pagination in an API?](#3-how-do-you-implement-efficient-pagination-in-an-api)
- [4. How do you handle a database that becomes very large?](#4-how-do-you-handle-a-database-that-becomes-very-large)
- [5. Why use a search engine like Elasticsearch?](#5-why-use-a-search-engine-like-elasticsearch)
- [6. What is the difference between a relational database and a search engine?](#6-what-is-the-difference-between-a-relational-database-and-a-search-engine)
- [7. How does search indexing work in Elasticsearch?](#7-how-does-search-indexing-work-in-elasticsearch)

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
