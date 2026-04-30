Q. Where can you store a JWT on the frontend? What are the security trade-offs of each?

There are four main ways to store a JWT on the frontend: localStorage, sessionStorage, cookies or an in-memory javascript variable.

localStorage and sessionStorage are two simple javascript object in the browser. The advantage is that they're easy to use, you don't need to configure anything, just store the JWT and send it as a header in your requests. The disadvantage is that they're stored directly in the javascript of the browser so they're vulnerable to XSS attacks.

sessionStorage is cleared when the tab is closed whereas localStorage persists until explicitly deleted. Because of that, sessionStorage is slightly safer than localStorage.

cookies are stored in a file on the client's machine. The advantage of cookies is that they're automatically stored by the browser and they're not vulnerable to XSS attacks if you use the `httpOnly` flag. However, they're automatically attached to every request by the browser which makes them vulnerable to CSRF attacks.

Finally, you could store the JWT on an in-memory variable like a React state. This would be the most secure against XSS and CSRF attacks since it's not persisted nor sent automatically. But because it's not persisted, it means it's cleared at each refresh which means user has to re-authenticate.