# What is CORS and how would you configure it correctly for a Python backend serving a frontend on a different domain?

To understand CORS, you first need to understand same-origin policy (SOP).

SOP is a security mechanism on the browser. The principle is simple : let's say you got unlucky and opened a malicious website whose domain is `http://evil.com`. This website ran a malicious script into your browser. Bad news, it already has access to your local storage, session storage and cookies... BUT those are only data related to the page it opened. What the attacker would like is to get access to any site in your browser (bank, social networks, email, etc). For this, it sends a request to those sites - e.g `bank.com` - and reads the response. 

That's where SOP plays its role. SOP prevents script running in one origin (protocol + domain + port) from reading data from another origin. 

Here, it means that the browser doesn't allow the malicious script running at `http://evil.com` from reading data coming from `http://bank.com`. SOP doesn't prevent from sending the request, but it prevents the frontend from reading the response.

Without SOP, an attacker could read any site in your browser after you opened just one malicious tab. This would be catastrophic.

SOP is useful but it becomes a problem when you are developing a frontend and a backend with different domains. For instance, `https://frontend.example.com` and `https://api.example.com`. Here, the browser won't allow your frontend to see the data sent by your backend.

The solution is to configure the mechanism that manages the interactions between different domains : cross-origin resource sharing or CORS.

It's a security mechanism implemented by browsers to control which domains can access resources from a different origin. By default, it applies the same-origin policy.

The solution is to configure CORS in the backend to define which origins are allowed to fetch resources.