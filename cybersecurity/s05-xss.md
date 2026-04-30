Q. What's an XSS ? Why is storing a JWT in sessionStorage vulnerable to XSS?

XSS or cross-site scripting is one of the most common web attack. It's when an attacker exploits a vulnerability on a website to inject a malicious Javascript script that is run by another user's browser.

For example, few years ago, a student discovered that it was possible to write a script inside a tweet. He was able to write a script that would automatically retweet its message to anyone seeing it.

The risk here is that in an XSS attack, the script is considered as regular code and has therefore the same rights as the webpage. Which means the script has access to localStorage, sessionStorage, document.cookie (if `httpOnly` flag hasn't been set), form inputs and DOM content.

So if a JWT is stored in sessionStorage, it could be retrieved by a malicious script, sent to the attacker and the attacker could then authenticate as the user to the server.