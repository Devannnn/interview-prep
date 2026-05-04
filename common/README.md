# Common — interview questions

## Table of contents

- [1. What are CPU-bound and I/O-bound tasks ?](#1-what-are-cpu-bound-and-io-bound-tasks)
- [2. What is CORS and how would you configure it correctly for a Python backend serving a frontend on a different domain?](#2-what-is-cors-and-how-would-you-configure-it-correctly-for-a-python-backend-serving-a-frontend-on-a-different-domain)
- [3. What are the FAIR data principles?](#3-what-are-the-fair-data-principles)
- [4. What happens when a metadata schema changes?](#4-what-happens-when-a-metadata-schema-changes)
- [5. How do you prevent breaking API consumers?](#5-how-do-you-prevent-breaking-api-consumers)
- [6. What is the difference between a VM and a container?](#6-what-is-the-difference-between-a-vm-and-a-container)
- [7. How would you write tests for an API?](#7-how-would-you-write-tests-for-an-api)
- [8. How do you migrate millions of records safely?](#8-how-do-you-migrate-millions-of-records-safely)
- [9. How do you handle a large data migration?](#9-how-do-you-handle-a-large-data-migration)
- [10. What is the difference between localStorage, sessionStorage, and cookies?](#10-what-is-the-difference-between-localstorage-sessionstorage-and-cookies)
- [11. What's the DOM ?](#11-whats-the-dom)

---

#### 1. What are CPU-bound and I/O-bound tasks ?

<details>
<summary>Reveal answer</summary>

The term X-bound designates a type of task which is limited by a specific ressource. It means this task is spending most of its time using that ressource and that its performance depends on the ressource’s access.

A CPU-bound task means that this task spends most of its time executing instructions on the CPU - for instance a program computing the decimals of pi. The CPU’s performance is the main bottleneck for this task. You improve the performance of a CPU-bound task by using multi-processing.

An I/O-bound task means that this task spends most its time waiting for external operations such as network, database or disk access. In that example, the disk’s performance is the main bottleneck for this task. You improve the performance of an I/O-bound task by using concurrency to keep executing operations during the waiting time.

</details>

---

#### 2. What is CORS and how would you configure it correctly for a Python backend serving a frontend on a different domain?

<details>
<summary>Reveal answer</summary>

To understand CORS, you first need to understand same-origin policy (SOP).

SOP is a security mechanism on the browser. The principle is simple : let's say you got unlucky and opened a malicious website whose domain is `http://evil.com`. This website ran a malicious script into your browser. Bad news, it already has access to your local storage, session storage and cookies... BUT those are only data related to the page it opened. What the attacker would like is to get access to any site in your browser (bank, social networks, email, etc). For this, it sends a request to those sites - e.g `bank.com` - and reads the response. 

That's where SOP plays its role. SOP prevents script running in one origin (protocol + domain + port) from reading data from another origin. 

Here, it means that the browser doesn't allow the malicious script running at `http://evil.com` from reading data coming from `http://bank.com`. SOP doesn't prevent from sending the request, but it prevents the frontend from reading the response.

Without SOP, an attacker could read any site in your browser after you opened just one malicious tab. This would be catastrophic.

SOP is useful but it becomes a problem when you are developing a frontend and a backend with different domains. For instance, `https://frontend.example.com` and `https://api.example.com`. Here, the browser won't allow your frontend to see the data sent by your backend.

The solution is to configure the mechanism that manages the interactions between different domains : cross-origin resource sharing or CORS.

It's a security mechanism implemented by browsers to control which domains can access resources from a different origin. By default, it applies the same-origin policy.

The solution is to configure CORS in the backend to define which origins are allowed to fetch resources.

</details>

---

#### 3. What are the FAIR data principles?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Checks if you understand open science expectations.
- Verifies that you can connect metadata quality to discoverability and reuse.

## Answer structure (keep it concise)
1. Define FAIR in one sentence.
2. Explain each principle in practical terms:
   - Findable
   - Accessible
   - Interoperable
   - Reusable
3. Give one concrete example from your experience.
4. Close with impact on reliability, collaboration, and long-term data value.

</details>

---

#### 4. What happens when a metadata schema changes?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Evaluates your understanding of backward compatibility and data integrity.
- Checks if you can evolve systems safely over time.

## Answer structure (keep it concise)
1. Describe risks: invalid records, broken APIs, migration complexity.
2. Explain safe rollout approach:
   - Version the schema
   - Add compatibility layer
   - Validate and migrate incrementally
3. Mention testing and rollback strategy.
4. Close with how you communicate changes across teams.

</details>

---

#### 5. How do you prevent breaking API consumers?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Evaluates your API lifecycle discipline and empathy for downstream users.
- Confirms you can ship changes safely in collaborative ecosystems.

## Answer structure (keep it concise)
1. State compatibility-first principle.
2. Describe concrete practices:
   - Versioning policy
   - Deprecation windows
   - Additive changes first
3. Explain safeguards:
   - Contract tests
   - Consumer feedback/testing
   - Release notes and migration guides
4. Share one case where you avoided or mitigated a breaking change.

</details>

---

#### 6. What is the difference between a VM and a container?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Checks your infrastructure fundamentals and deployment reasoning.
- Verifies that you understand isolation, performance, and operations trade-offs.

## Answer structure (keep it concise)
1. Give a clear one-line distinction.
2. Compare architecture:
   - VM: virtualized hardware + guest OS
   - Container: isolated processes sharing host kernel
3. Compare trade-offs:
   - Startup time
   - Resource overhead
   - Isolation strength
4. End with when you would choose each in production.

</details>

---

#### 7. How would you write tests for an API?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Assesses engineering quality standards and reliability focus.
- Checks if you can balance speed, confidence, and realism.

## Answer structure (keep it concise)
1. Separate test layers: unit, integration, end-to-end smoke.
2. Validate status codes, payload contracts, and error paths.
3. Use isolated test data/mocked dependencies where appropriate.
4. Mention CI execution and fast feedback loops.

</details>

---

#### 8. How do you migrate millions of records safely?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Assesses your production mindset for scale, reliability, and recovery.
- Verifies that you can balance safety, speed, and observability.

## Answer structure (keep it concise)
1. Start with migration goals and failure risks.
2. Describe execution strategy:
   - Batch processing and idempotency
   - Checkpoints and retry logic
   - Shadow/dual writes if needed
3. Explain validation:
   - Row counts and checksums
   - Sampling and business-rule verification
4. End with rollout, monitoring, and rollback plan.

</details>

---

#### 9. How do you handle a large data migration?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Evaluates production safety, risk management, and execution rigor.
- Highly plausible for large repository transitions.

## Answer structure (keep it concise)
1. Plan scope, dependencies, and acceptance criteria first.
2. Build migration scripts with idempotency and checkpoints.
3. Validate data correctness (counts, checksums, business rules).
4. Use progressive rollout, monitoring, and rollback strategy.

</details>

---

#### 10. What is the difference between localStorage, sessionStorage, and cookies?

<details>
<summary>Reveal answer</summary>

Localstorage, sessionStorage and cookies are all ways to store user-specific data to provide a more custom experience.

LocalStorage is a local storage for your browser. It stores data permanently which means those data are persisted between page reloads and browser restarts. It can save as much as 10 Mb. It's not cleared automatically - the cache needs to be cleared. Only the client-side reads this storage.

SessionStorage stores data temporarily, until you close the tab or the window. It's a bit smaller - 5 Mb. Only the client-side reads this storage.

Cookies are very tiny data - 4 Kb - stored in the browser and which are sent to the server at each HTTP request.

</details>

---

#### 11. What's the DOM ?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---
