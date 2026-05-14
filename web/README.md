# Web — interview questions

## Table of contents

- [1. What's the DOM ?](#1-whats-the-dom)
- [2. What is the HTTP request/response lifecycle?](#2-what-is-the-http-requestresponse-lifecycle)
- [3. What happens when you type a URL in the browser and press enter?](#3-what-happens-when-you-type-a-url-in-the-browser-and-press-enter)
- [4. What is the difference between 400, 401, 403, and 404?](#4-what-is-the-difference-between-400-401-403-and-404)
- [5. What is the difference between localStorage, sessionStorage, and cookies?](#5-what-is-the-difference-between-localstorage-sessionstorage-and-cookies)
- [6. What makes an API RESTful?](#6-what-makes-an-api-restful)
- [7. Difference between PUT, PATCH, and POST?](#7-difference-between-put-patch-and-post)
- [8. How would you write tests for an API?](#8-how-would-you-write-tests-for-an-api)
- [9. How do you write a unit test for a function that calls an external API, without actually hitting the API?](#9-how-do-you-write-a-unit-test-for-a-function-that-calls-an-external-api-without-actually-hitting-the-api)
- [10. In a unit test for a service that calls an external payment API, what would you mock and why?](#10-in-a-unit-test-for-a-service-that-calls-an-external-payment-api-what-would-you-mock-and-why)

---

#### 1. What's the DOM ?

<details>
<summary>Reveal answer</summary>

The Document Object Model (DOM) is a data structure that represents an HTML document.

What is the DOM for ? The DOM is there so programming languages are able to modify the document.

Javascript cannot directly modify the HTML source file. So how do you make a page interactive ? You use an intermediate that is created from the HTML, that can be modified by Javascript and that can be rendered by a browser. This is the DOM.

The DOM is an in-memory representation of an HTML document. It's represented by a tree where each node is an element of the HTML document.

</details>

---

#### 2. What is the HTTP request/response lifecycle?

<details>
<summary>Reveal answer</summary>

A client sends an HTTP request to a server over the network. The request includes things like the HTTP method, URL/path, headers, and sometimes a body.

The server receives the request, routes it to the correct handler, processes it, and sends back an HTTP response. The response includes a status code, headers, and usually a body.

The client receives the response and handles it, for example by rendering HTML, parsing JSON, updating the UI, or showing an error.

</details>

---

#### 3. What happens when you type a URL in the browser and press enter?

<details>
<summary>Reveal answer</summary>

When you type a URL and press enter, the browser first parses the URL to identify the protocol, domain, path, and other parts.

The browser resolves the domain name by sending a request to the closest DNS to get the IP.

Once it has the IP address, the browser opens a connection to the server. For HTTPS, it establishes a TCP connection and performs a TLS handshake.

The browser then sends an HTTP request to the server. The request is routed over the network to the target server, which processes it and sends back an HTTP response.

Finally, the browser receives the response, parses the HTML, builds the DOM, loads additional assets like CSS and JavaScript, and renders the page.

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

#### 6. What makes an API RESTful?

<details>
<summary>Reveal answer</summary>

A RESTful API is an API designed around resources, usually exposed through URLs such as `/users` or `/orders/123`.

It uses standard HTTP methods to operate on those resources: `GET` to read, `POST` to create, `PUT` or `PATCH` to update, and `DELETE` to remove.

It should be stateless, meaning each request contains enough information for the server to process it without relying on hidden client-specific state between requests.

A RESTful API also uses HTTP status codes consistently and usually returns resource representations such as JSON.

</details>

---

#### 7. Difference between PUT, PATCH, and POST?

<details>
<summary>Reveal answer</summary>

POST is used to create a new resource.

PATCH is used to partially update an existing resource. With a PATCH request, you send only the fields you want to update.

PUT is used to replace an existing resource entirely. With a PUT request, you send the entire new object. On some APIs, if the existing resource doesn't exist, the PUT request will create it.

The difference is that a POST request is usually not idempotent, whereas a PUT request usually is. It means that if you send the same POST request twice, you may create two resources or trigger the same action twice. If you send the same PUT request twice, the resource should end up in the same final state.

</details>

---

#### 8. How would you write tests for an API?

<details>
<summary>Reveal answer</summary>

I would write tests for each important API endpoint and cover both successful and failing cases.

For each endpoint, I would check that the API returns the expected status code, response body, headers if relevant, and that it correctly updates or reads data from the database.

I would test validation errors and edge cases, such as missing fields, invalid input, nonexistent resources, duplicate resources, and wrong HTTP methods.

I would also test authentication and authorization: unauthenticated users should get `401`, authenticated users without permission should get `403`, and authorized users should be able to access the resource.

When needed, I would use a test database and mock external services so the tests are reliable and do not depend on real third-party APIs.

</details>

---

#### 9. How do you write a unit test for a function that calls an external API, without actually hitting the API?

<details>
<summary>Reveal answer</summary>

I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.

</details>

---

#### 10. In a unit test for a service that calls an external payment API, what would you mock and why?

<details>
<summary>Reveal answer</summary>

I would mock the external payment client or HTTP request and make it return a realistic fake response. The goal is to test my service logic without depending on the real payment API, network, credentials, or provider availability. Besides the return value, I would verify that the payment client was called with the correct parameters, and I would test how the service behaves when the payment API returns an error or times out.

</details>

