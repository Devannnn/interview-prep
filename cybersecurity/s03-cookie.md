Q. What's a cookie ?

A cookie is a small piece of data sent by a server to a browser via a response with a `Set-Cookie` header. The browser stores it on the client's machine and includes it in the header of all the subsequent requests to this subdomain. Cookies can be used for many things - identification, user preferences, tracking - and can be configured using flags to manage their behavior.

The main difference between cookies and other storage mechanisms like localStorage or sessionStorage is that they are automatic. The browser stores them automatically on reception and attaches them automatically to the requests - without any javascript involved.