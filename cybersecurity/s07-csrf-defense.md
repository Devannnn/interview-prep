Q. How do you protect against CSRF when your JWT is in an httpOnly cookie? 

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