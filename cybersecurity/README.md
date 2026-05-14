# Cybersecurity — interview questions

## Table of contents

- [1. What's the difference between identification, authentication and authorization ?](#1-whats-the-difference-between-identification-authentication-and-authorization)
- [2. What's a cookie ?](#2-whats-a-cookie)
- [3. What's a JWT ?](#3-whats-a-jwt)
- [4. What's an XSS ? Why is storing a JWT in sessionStorage vulnerable to XSS?](#4-whats-an-xss-why-is-storing-a-jwt-in-sessionstorage-vulnerable-to-xss)
- [5. What's a CSRF ? Why would storing a JWT in an httpOnly cookie make it immune to XSS but exposed to CSRF?](#5-whats-a-csrf-why-would-storing-a-jwt-in-an-httponly-cookie-make-it-immune-to-xss-but-exposed-to-csrf)
- [6. Where can you store a JWT on the frontend? What are the security trade-offs of each?](#6-where-can-you-store-a-jwt-on-the-frontend-what-are-the-security-trade-offs-of-each)
- [7. How do you protect against CSRF when your JWT is in an httpOnly cookie?](#7-how-do-you-protect-against-csrf-when-your-jwt-is-in-an-httponly-cookie)
- [8. What is CORS and how would you configure it correctly for a backend serving a frontend on a different domain?](#8-what-is-cors-and-how-would-you-configure-it-correctly-for-a-backend-serving-a-frontend-on-a-different-domain)
- [9. Why is it usually a bad idea for a GET endpoint to modify data?](#9-why-is-it-usually-a-bad-idea-for-a-get-endpoint-to-modify-data)
- [10. Session-based auth vs token-based auth?](#10-session-based-auth-vs-token-based-auth)
- [11. Access token vs refresh token?](#11-access-token-vs-refresh-token)
- [12. How do you store passwords securely?](#12-how-do-you-store-passwords-securely)
- [13. How do you avoid leaking sensitive data in logs/errors?](#13-how-do-you-avoid-leaking-sensitive-data-in-logserrors)

---

#### 1. What's the difference between identification, authentication and authorization ?

<details>
<summary>Reveal answer</summary>

Identification is the answer to "Who are you?". When you enter your username on a form, you are identifying yourself. It's not a proof, just a claim.

Authentication is the answer to "Prove it". When you authenticate, you prove you are who you claim to be. You do this by entering your password, scanning your fingerprint or providing a 2FA code.

Authorization is the answer to "What are you allowed to do". After a server verifies who you are, it doesn't mean that you should be able to perform any actions. At each request, the server checks your role and permissions to see what you're allowed to access.

</details>

---

#### 2. What's a cookie ?

<details>
<summary>Reveal answer</summary>

A cookie is a small piece of data sent by a server to a browser via a response with a `Set-Cookie` header. The browser stores it on the client's machine and includes it in the header of all the subsequent requests to this subdomain. Cookies can be used for many things - identification, user preferences, tracking - and can be configured using flags to manage their behavior.

The main difference between cookies and other storage mechanisms like localStorage or sessionStorage is that they are automatic. The browser stores them automatically on reception and attaches them automatically to the requests - without any javascript involved.

</details>

---

#### 3. What's a JWT ?

<details>
<summary>Reveal answer</summary>

# Why does it exist ?
When a user connects to a server, they use credentials like a username and a password.

This allows the server to match the user with the data stored.

It works fine but HTTP requests are stateless i.e. they forget who you are after each request.

Which means, you need a way to identify yourself to the server at EACH request.

We could send our credentials alongside all our requests but then we'll need to constantly have them in plain stored by the client - which would be extremely vulnerable.

Instead we are using another system: 
- the client first log in using their credentials ;
- the server verify the credentials and, if they are correct, returns a JWT ;
- the client uses this JWT to perform the following requests.

So JWT are merely a way to identify a client without exposing their credentials.

# Definition
A JWT is a way to transmit claims (identity information) safely and compactely between a client and a server in a URL-compatible way.

A JWT has three parts - a header, a payload and a signature - which are all encoded in base64 and separated by a dot.

The header contains the signing algorithm used to create the signature. The payload contains the data identifying the user. The signature contains the header+payload hashed using the secret key of the server.

# Why is it secure ?
First, the payload contains no credentials. It's only encoded in base64 so it could be easily decoded by an attacker. Instead, the payload contains identity information like `user_id: 42` which makes sense for the server but has no value for an attacker.

Second, because of the signature, an attacker cannot create or modify a token. Even if the attacker can easily see and modify the payload, it cannot resign it without the secret key. Which means any fake token would be immediately noticed by the server.

</details>

---

#### 4. What's an XSS ? Why is storing a JWT in sessionStorage vulnerable to XSS?

<details>
<summary>Reveal answer</summary>

XSS or cross-site scripting is one of the most common web attack. It's when an attacker exploits a vulnerability on a website to inject a malicious Javascript script that is run by another user's browser.

For example, few years ago, a student discovered that it was possible to write a script inside a tweet. He was able to write a script that would automatically retweet its message to anyone seeing it.

The risk here is that in an XSS attack, the script is considered as regular code and has therefore the same rights as the webpage. Which means the script has access to localStorage, sessionStorage, document.cookie (if `httpOnly` flag hasn't been set), form inputs and DOM content.

So if a JWT is stored in sessionStorage, it could be retrieved by a malicious script, sent to the attacker and the attacker could then authenticate as the user to the server.

</details>

---

#### 5. What's a CSRF ? Why would storing a JWT in an httpOnly cookie make it immune to XSS but exposed to CSRF?

<details>
<summary>Reveal answer</summary>

A CSRF, or Cross-Site Request Forgery, is an attack where a malicious site causes the user’s browser to send an authenticated request to another site where the user is already logged in.

This attack takes advantage of a core feature of cookies: they're attached automatically to the request by the browser.

For instance, Alice sends an image to Bob on a forum. The /src path of this image is `https://bank.com/transfer?to=alice&amount=1000`. Bob opens the image. His browser tries to load the image which actually performs a GET request to Bob's bank account. Because Bob has a cookie stored in his browser, this cookie is sent alongside the request and it succeeds.

Now coming back to storing JWT in a cookie instead of localStorage/sessionStorage.

Storing a JWT in a httpOnly cookie protects it from XSS attacks because javascript cannot access httpOnly cookies. But, it means that those cookies are sent automatically by the browser and could therefore be used by a CSRF attack. 

The key difference between XSS and CSRF here is that CSRF is a blind-attack. XSS allows the attacker to see and retrieve sensitive information from the victim's browser. On the other hand, in a CSRF attack, the attacker never sees the cookie nor the result from the request because all was done by the victim's browser. But the action was performed. XSS is used to steal information whereas CSRF is used to perform malicious actions.

</details>

---

#### 6. Where can you store a JWT on the frontend? What are the security trade-offs of each?

<details>
<summary>Reveal answer</summary>

There are four main ways to store a JWT on the frontend: localStorage, sessionStorage, cookies or an in-memory javascript variable.

localStorage and sessionStorage are two simple javascript object in the browser. The advantage is that they're easy to use, you don't need to configure anything, just store the JWT and send it as a header in your requests. The disadvantage is that they're stored directly in the javascript of the browser so they're vulnerable to XSS attacks.

sessionStorage is cleared when the tab is closed whereas localStorage persists until explicitly deleted. Because of that, sessionStorage is slightly safer than localStorage.

cookies are stored in a file on the client's machine. The advantage of cookies is that they're automatically stored by the browser and they're not vulnerable to XSS attacks if you use the `httpOnly` flag. However, they're automatically attached to every request by the browser which makes them vulnerable to CSRF attacks.

Finally, you could store the JWT on an in-memory variable like a React state. This would be the most secure against XSS and CSRF attacks since it's not persisted nor sent automatically. But because it's not persisted, it means it's cleared at each refresh which means user has to re-authenticate.

</details>

---

#### 7. How do you protect against CSRF when your JWT is in an httpOnly cookie?

<details>
<summary>Reveal answer</summary>

The most common defense is the double submit pattern which uses a second token called a CSRF token.

The problem at the root of CSRF attacks is that the server is not able to tell if the request was issued by the frontend or by a malicious website.

That's when CSRF tokens come in.

The idea is simple. When the user authenticates, the server issues a random second token. This token is sent to the frontend which stores it. This token must be attached **manually** by the frontend at every request either in the body or in the headers.

That way, even if an attacker tricks the victim's browser into sending the request, it won't include the CSRF token and will be flagged by the server as a malicious request.

Another solution is to issue the first httpOnly cookie with the flag `SameSite`. Setting `SameSite=Strict` or `SameSite=Lax` prevents the browser from attaching the cookie to a request that originates from a different site. 

In practice, applications use both CSRF tokens and SameSite cookies.

Why use both ? Isn't SameSite enough ? If it ensures that the cookie will only be attached to a query coming from the site that issued it, then the double submit pattern offers no additional protection. No ?

For several reasons:
1. Because the `SameSite` flag is a defense on the browser's side whereas CSRF is a defense on the server's side. If the browser has an issue, e.g. doesn't respect the `SameSite` flag, then you would be vulnerable to CSRF attacks.

2. Because if you use `SameSite=Lax`, which is the most common, the browser still automatically includes cookies on GET requests. Then if the server performs state-changing actions on GET requests, it would be vulnerable.

</details>

---

#### 8. What is CORS and how would you configure it correctly for a backend serving a frontend on a different domain?

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

#### 9. Why is it usually a bad idea for a GET endpoint to modify data?

<details>
<summary>Reveal answer</summary>

`GET` should be **safe** and **idempotent**. "Safe" means it should not modify server state. "Idempotent" means repeating the same request should have the same effect. A mutating `GET` is risky because browsers, crawlers, caches, link previews, or proxies may call `GET` requests automatically. Also it exposes the application to **CSRF** attacks.

</details>

---

#### 10. Session-based auth vs token-based auth?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 11. Access token vs refresh token?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 12. How do you store passwords securely?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 13. How do you avoid leaking sensitive data in logs/errors?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>
