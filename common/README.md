# Common — interview questions

## Table of contents

- [1. What's the DOM ?](#1-whats-the-dom)
- [2. What is the HTTP request/response lifecycle?](#2-what-is-the-http-requestresponse-lifecycle)
- [3. What happens when you type a URL in the browser and press enter?](#3-what-happens-when-you-type-a-url-in-the-browser-and-press-enter)
- [4. What is the difference between 400, 401, 403, and 404?](#4-what-is-the-difference-between-400-401-403-and-404)
- [5. What is the difference between localStorage, sessionStorage, and cookies?](#5-what-is-the-difference-between-localstorage-sessionstorage-and-cookies)
- [6. What are CPU-bound and I/O-bound tasks ?](#6-what-are-cpu-bound-and-io-bound-tasks)
- [7. What makes an API RESTful?](#7-what-makes-an-api-restful)
- [8. Difference between PUT, PATCH, and POST?](#8-difference-between-put-patch-and-post)
- [9. How would you write tests for an API?](#9-how-would-you-write-tests-for-an-api)
- [10. How do you write a unit test for a function that calls an external API, without actually hitting the API?](#10-how-do-you-write-a-unit-test-for-a-function-that-calls-an-external-api-without-actually-hitting-the-api)
- [11. In a unit test for a service that calls an external payment API, what would you mock and why?](#11-in-a-unit-test-for-a-service-that-calls-an-external-payment-api-what-would-you-mock-and-why)
- [12. What is the difference between a VM and a container?](#12-what-is-the-difference-between-a-vm-and-a-container)
- [13. Imagine your code works locally, but fails in production. What are some possible reasons, and how would you investigate?](#13-imagine-your-code-works-locally-but-fails-in-production-what-are-some-possible-reasons-and-how-would-you-investigate)
- [14. A bug only happens sometimes in production and you cannot reproduce it locally. What steps would you take to investigate? What extra logging or monitoring would help you without exposing sensitive data?](#14-a-bug-only-happens-sometimes-in-production-and-you-cannot-reproduce-it-locally-what-steps-would-you-take-to-investigate-what-extra-logging-or-monitoring-would-help-you-without-exposing-sensitive-data)

---

#### 1. What's the DOM ?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 2. What is the HTTP request/response lifecycle?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 3. What happens when you type a URL in the browser and press enter?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 4. What is the difference between 400, 401, 403, and 404?

<details>
<summary>Reveal answer</summary>

- `400 Bad Request`: the request is invalid, malformed, or fails validation.
- `401 Unauthorized`: the user is **not authenticated** or has invalid/missing credentials. Despite the name, it means "you need to log in or provide valid credentials."
- `403 Forbidden`: the user is **authenticated**, but does not have permission to access the resource.
- `404 Not Found`: the resource does not exist, or sometimes the API intentionally hides its existence.

</details>

---

#### 5. What is the difference between localStorage, sessionStorage, and cookies?

<details>
<summary>Reveal answer</summary>

Localstorage, sessionStorage and cookies are all ways to store user-specific data to provide a more custom experience.

LocalStorage is a local storage for your browser. It stores data permanently which means those data are persisted between page reloads and browser restarts. It can save as much as 10 Mb. It's not cleared automatically - the cache needs to be cleared. Only the client-side reads this storage.

SessionStorage stores data temporarily, until you close the tab or the window. It's a bit smaller - 5 Mb. Only the client-side reads this storage.

Cookies are very tiny data - 4 Kb - stored in the browser and which are sent to the server at each HTTP request.

</details>

---

#### 6. What are CPU-bound and I/O-bound tasks ?

<details>
<summary>Reveal answer</summary>

The term X-bound designates a type of task which is limited by a specific ressource. It means this task is spending most of its time using that ressource and that its performance depends on the ressource's access.

A CPU-bound task means that this task spends most of its time executing instructions on the CPU - for instance a program computing the decimals of pi. The CPU's performance is the main bottleneck for this task. You improve the performance of a CPU-bound task by using multi-processing.

An I/O-bound task means that this task spends most its time waiting for external operations such as network, database or disk access. In that example, the disk's performance is the main bottleneck for this task. You improve the performance of an I/O-bound task by using concurrency to keep executing operations during the waiting time.

</details>

---

#### 7. What makes an API RESTful?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 8. Difference between PUT, PATCH, and POST?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 9. How would you write tests for an API?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 10. How do you write a unit test for a function that calls an external API, without actually hitting the API?

<details>
<summary>Reveal answer</summary>

I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.

</details>

---

#### 11. In a unit test for a service that calls an external payment API, what would you mock and why?

<details>
<summary>Reveal answer</summary>

I would mock the external payment client or HTTP request and make it return a realistic fake response. The goal is to test my service logic without depending on the real payment API, network, credentials, or provider availability. Besides the return value, I would verify that the payment client was called with the correct parameters, and I would test how the service behaves when the payment API returns an error or times out.

</details>

---

#### 12. What is the difference between a VM and a container?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 13. Imagine your code works locally, but fails in production. What are some possible reasons, and how would you investigate?

<details>
<summary>Reveal answer</summary>

Possible reasons include different environment variables, dependency versions, interpreter version, database schema, CORS/auth settings, etc.

I would first check the production error message, logs, and stack trace to understand where it fails. Then I would compare local and production environments to identify any differences. If logs are not enough, I would add targeted logs, then try to reproduce locally.

</details>

---

#### 14. A bug only happens sometimes in production and you cannot reproduce it locally. What steps would you take to investigate? What extra logging or monitoring would help you without exposing sensitive data?

<details>
<summary>Reveal answer</summary>

I would start by checking the stack trace and production logs around the failure. Then I would look for patterns: affected users, request payloads, timestamps, specific servers, database records, feature flags, or load spikes. If logs are not enough, I would add targeted logging with correlation/request IDs, but avoid logging secrets or personal data. I would also compare local and production configuration, dependency versions, database schema, environment variables, and external service behavior.

</details>
