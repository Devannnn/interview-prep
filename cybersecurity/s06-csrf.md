Q. What's a CSRF ? Why would storing a JWT in an httpOnly cookie make it immune to XSS but exposed to CSRF?

A CSRF is a kind of attack where an attacker tricks the victim's browser into sending an HTTP request to a target website *on behalf of the user*.

This attack takes advantage of a core feature of cookies: they're attached automatically to the request by the browser.

For instance, Alice sends an image to Bob on a forum. The /src path of this image is `https://bank.com/transfer?to=alice&amount=1000`. Bob opens the image. His browser tries to load the image which actually performs a GET request to Bob's bank account. Because Bob has a cookie stored in his browser, this cookie is sent alongside the request and it succeeds.

Now coming back to storing JWT in a cookie instead of localStorage/sessionStorage.

Storing a JWT in a httpOnly cookie protects it from XSS attacks because javascript cannot access httpOnly cookies. But, it means that those cookies are sent automatically by the browser and could therefore be used by a CSRF attack. 

The key difference between XSS and CSRF here is that CSRF is a blind-attack. XSS allows the attacker to see and retrieve sensitive information from the victim's browser. On the other hand, in a CSRF attack, the attacker never sees the cookie nor the result from the request because all was done by the victim's browser. But the action was performed. XSS is used to steal information whereas CSRF is used to perform malicious actions.
