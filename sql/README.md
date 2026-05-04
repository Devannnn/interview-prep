# SQL — interview questions

## Table of contents

- [1. What is an SQL index and why is it useful?](#1-what-is-an-sql-index-and-why-is-it-useful)
- [2. What is the difference between INNER JOIN and LEFT JOIN?](#2-what-is-the-difference-between-inner-join-and-left-join)
- [3. How do you handle a database that becomes very large?](#3-how-do-you-handle-a-database-that-becomes-very-large)
- [4. How do you implement efficient pagination in an API?](#4-how-do-you-implement-efficient-pagination-in-an-api)
- [5. Why use a search engine like Elasticsearch?](#5-why-use-a-search-engine-like-elasticsearch)
- [6. What is the difference between a relational database and a search engine?](#6-what-is-the-difference-between-a-relational-database-and-a-search-engine)
- [7. How does search indexing work in Elasticsearch?](#7-how-does-search-indexing-work-in-elasticsearch)

---

#### 1. What is an SQL index and why is it useful?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Tests database performance fundamentals.
- Checks if you understand read/write trade-offs.

## Answer structure (keep it concise)
1. Define index as a structure accelerating row lookup.
2. Explain gains for search/sort/join patterns.
3. Mention cost: extra storage and slower writes/updates.
4. Give one example of choosing indexes from real query patterns.

</details>

---

#### 2. What is the difference between INNER JOIN and LEFT JOIN?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Verifies SQL reasoning accuracy.
- Checks if you understand result-set semantics in real business cases.

## Answer structure (keep it concise)
1. `INNER JOIN`: keeps only matching rows on both sides.
2. `LEFT JOIN`: keeps all left rows, plus matches from right.
3. Explain `NULL` behavior for non-matching right-side data.
4. Give one practical scenario for each join type.

</details>

---

#### 3. How do you handle a database that becomes very large?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Assesses scalability strategy and operational maturity.
- Relevant to long-term repository growth.

## Answer structure (keep it concise)
1. Start with bottleneck identification (queries, storage, contention).
2. Apply foundational levers:
   - Indexing and query tuning
   - Pagination/read patterns
   - Partitioning/archiving
   - Caching for hot reads
3. Mention monitoring and capacity planning.
4. Explain incremental rollout with measurable checkpoints.

</details>

---

#### 4. How do you implement efficient pagination in an API?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Tests API performance and client usability thinking.
- Important for large catalogs and search results.

## Answer structure (keep it concise)
1. Explain baseline `LIMIT/OFFSET` approach and its limits at scale.
2. Introduce cursor/keyset pagination for large datasets.
3. Define stable sort order and consistent page tokens.
4. Mention metadata (`next_cursor`, total count when needed) and edge cases.

</details>

---

#### 5. Why use a search engine like Elasticsearch?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Checks if you understand when DB search is not enough.
- Directly relevant for InvenioRDM and discovery workflows.

## Answer structure (keep it concise)
1. Explain full-text search capabilities vs basic SQL text matching.
2. Describe indexing and relevance scoring benefits.
3. Mention scalability/performance for search-heavy workloads.
4. Add trade-offs: eventual consistency, ops complexity, sync with source DB.

</details>

---

#### 6. What is the difference between a relational database and a search engine?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Evaluates architectural judgment, not just definitions.
- Important for systems combining transactional integrity and discovery.

## Answer structure (keep it concise)
1. Define relational DB strengths: transactions, consistency, joins, constraints.
2. Define search engine strengths: full-text, relevance ranking, flexible search.
3. Explain complementary architecture: DB as source of truth, search index for discovery.
4. Mention data-sync and consistency trade-offs clearly.

</details>

---

#### 7. How does search indexing work in Elasticsearch?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Tests your ability to reason about search relevance and performance.
- Checks if you understand analyzers, mappings, and query behavior.

## Answer structure (keep it concise)
1. Explain that data is split into documents and inverted indexes.
2. Cover ingestion pipeline basics:
   - Mapping
   - Analysis (tokenization, filters)
   - Index refresh behavior
3. Explain query-time relevance at a high level.
4. Mention one practical optimization or trade-off you handled.

</details>

---
