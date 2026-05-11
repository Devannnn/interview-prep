# Common — interview questions

## Table of contents

- [1. What's the DOM ?](#1-whats-the-dom)
- [2. What are CPU-bound and I/O-bound tasks ?](#2-what-are-cpu-bound-and-io-bound-tasks)
- [3. What is the difference between localStorage, sessionStorage, and cookies?](#3-what-is-the-difference-between-localstorage-sessionstorage-and-cookies)
- [4. Why is it usually a bad idea for a GET endpoint to modify data?](#4-why-is-it-usually-a-bad-idea-for-a-get-endpoint-to-modify-data)
- [5. What is the difference between 400, 401, 403, and 404?](#5-what-is-the-difference-between-400-401-403-and-404)
- [6. What is CORS and how would you configure it correctly for a Python backend serving a frontend on a different domain?](#6-what-is-cors-and-how-would-you-configure-it-correctly-for-a-python-backend-serving-a-frontend-on-a-different-domain)
- [7. What is the difference between a VM and a container?](#7-what-is-the-difference-between-a-vm-and-a-container)
- [8. What are the FAIR data principles?](#8-what-are-the-fair-data-principles)
- [9. What happens when a metadata schema changes?](#9-what-happens-when-a-metadata-schema-changes)
- [10. How do you prevent breaking API consumers?](#10-how-do-you-prevent-breaking-api-consumers)
- [11. How would you write tests for an API?](#11-how-would-you-write-tests-for-an-api)
- [12. Imagine your code works locally, but fails in production. What are some possible reasons, and how would you investigate?](#12-imagine-your-code-works-locally-but-fails-in-production-what-are-some-possible-reasons-and-how-would-you-investigate)
- [13. A bug only happens sometimes in production and you cannot reproduce it locally. What steps would you take to investigate? What extra logging or monitoring would help you without exposing sensitive data?](#13-a-bug-only-happens-sometimes-in-production-and-you-cannot-reproduce-it-locally-what-steps-would-you-take-to-investigate-what-extra-logging-or-monitoring-would-help-you-without-exposing-sensitive-data)
- [14. How do you migrate millions of records safely?](#14-how-do-you-migrate-millions-of-records-safely)
- [15. How do you handle a large data migration?](#15-how-do-you-handle-a-large-data-migration)
- [16. In a unit test for a service that calls an external payment API, what would you mock and why?](#16-in-a-unit-test-for-a-service-that-calls-an-external-payment-api-what-would-you-mock-and-why)
- [17. What makes an API RESTful?](#17-what-makes-an-api-restful)
- [18. Difference between PUT, PATCH, and POST?](#18-difference-between-put-patch-and-post)
- [19. Session-based auth vs token-based auth?](#19-session-based-auth-vs-token-based-auth)
- [20. Access token vs refresh token?](#20-access-token-vs-refresh-token)
- [21. How do you store passwords securely?](#21-how-do-you-store-passwords-securely)
- [22. How do you avoid leaking sensitive data in logs/errors?](#22-how-do-you-avoid-leaking-sensitive-data-in-logserrors)
- [23. What happens when you type a URL in the browser and press enter?](#23-what-happens-when-you-type-a-url-in-the-browser-and-press-enter)
- [24. What is the HTTP request/response lifecycle?](#24-what-is-the-http-requestresponse-lifecycle)
- [25. What is the difference between authentication and authorization?](#25-what-is-the-difference-between-authentication-and-authorization)
- [26. How do you write a unit test for a function that calls an external API, without actually hitting the API?](#26-how-do-you-write-a-unit-test-for-a-function-that-calls-an-external-api-without-actually-hitting-the-api)

---

#### 1. What's the DOM ?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 2. What are CPU-bound and I/O-bound tasks ?

<details>
<summary>Reveal answer</summary>

The term X-bound designates a type of task which is limited by a specific ressource. It means this task is spending most of its time using that ressource and that its performance depends on the ressource’s access.

A CPU-bound task means that this task spends most of its time executing instructions on the CPU - for instance a program computing the decimals of pi. The CPU’s performance is the main bottleneck for this task. You improve the performance of a CPU-bound task by using multi-processing.

An I/O-bound task means that this task spends most its time waiting for external operations such as network, database or disk access. In that example, the disk’s performance is the main bottleneck for this task. You improve the performance of an I/O-bound task by using concurrency to keep executing operations during the waiting time.

</details>

---

#### 3. What is the difference between localStorage, sessionStorage, and cookies?

<details>
<summary>Reveal answer</summary>

Localstorage, sessionStorage and cookies are all ways to store user-specific data to provide a more custom experience.

LocalStorage is a local storage for your browser. It stores data permanently which means those data are persisted between page reloads and browser restarts. It can save as much as 10 Mb. It's not cleared automatically - the cache needs to be cleared. Only the client-side reads this storage.

SessionStorage stores data temporarily, until you close the tab or the window. It's a bit smaller - 5 Mb. Only the client-side reads this storage.

Cookies are very tiny data - 4 Kb - stored in the browser and which are sent to the server at each HTTP request.

</details>

---

#### 4. Why is it usually a bad idea for a GET endpoint to modify data?

<details>
<summary>Reveal answer</summary>

`GET` should be **safe** and **idempotent**. “Safe” means it should not modify server state. “Idempotent” means repeating the same request should have the same effect. A mutating `GET` is risky because browsers, crawlers, caches, link previews, or proxies may call `GET` requests automatically. Also it exposes the application to **CSRF** attacks.

</details>

---

#### 5. What is the difference between 400, 401, 403, and 404?

<details>
<summary>Reveal answer</summary>

- `400 Bad Request`: the request is invalid, malformed, or fails validation.
- `401 Unauthorized`: the user is **not authenticated** or has invalid/missing credentials. Despite the name, it means “you need to log in or provide valid credentials.”
- `403 Forbidden`: the user **is authenticated**, but does not have permission to access the resource.
- `404 Not Found`: the resource does not exist, or sometimes the API intentionally hides its existence.

</details>

---

#### 6. What is CORS and how would you configure it correctly for a Python backend serving a frontend on a different domain?

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

#### 7. What is the difference between a VM and a container?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 8. What are the FAIR data principles?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 9. What happens when a metadata schema changes?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 10. How do you prevent breaking API consumers?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 11. How would you write tests for an API?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 12. Imagine your code works locally, but fails in production. What are some possible reasons, and how would you investigate?

<details>
<summary>Reveal answer</summary>

Possible reasons include different environment variables, dependency versions, interpreter version, database schema, CORS/auth settings, etc.

I would first check the production error message, logs, and stack trace to understand where it fails. Then I would compare local and production environments to identify any differences. If logs are not enough, I would add targeted logs, then try to reproduce locally.

</details>

---

#### 13. A bug only happens sometimes in production and you cannot reproduce it locally. What steps would you take to investigate? What extra logging or monitoring would help you without exposing sensitive data?

<details>
<summary>Reveal answer</summary>

I would start by checking the stack trace and production logs around the failure. Then I would look for patterns: affected users, request payloads, timestamps, specific servers, database records, feature flags, or load spikes. If logs are not enough, I would add targeted logging with correlation/request IDs, but avoid logging secrets or personal data. I would also compare local and production configuration, dependency versions, database schema, environment variables, and external service behavior.

</details>

---

#### 14. How do you migrate millions of records safely?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 15. How do you handle a large data migration?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 16. In a unit test for a service that calls an external payment API, what would you mock and why?

<details>
<summary>Reveal answer</summary>

I would mock the external payment client or HTTP request and make it return a realistic fake response. The goal is to test my service logic without depending on the real payment API, network, credentials, or provider availability. Besides the return value, I would verify that the payment client was called with the correct parameters, and I would test how the service behaves when the payment API returns an error or times out.

</details>

---

#### 17. What makes an API RESTful?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 18. Difference between PUT, PATCH, and POST?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 19. Session-based auth vs token-based auth?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 20. Access token vs refresh token?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 21. How do you store passwords securely?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 22. How do you avoid leaking sensitive data in logs/errors?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 23. What happens when you type a URL in the browser and press enter?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 24. What is the HTTP request/response lifecycle?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 25. What is the difference between authentication and authorization?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 26. How do you write a unit test for a function that calls an external API, without actually hitting the API?

<details>
<summary>Reveal answer</summary>

I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.

</details>
