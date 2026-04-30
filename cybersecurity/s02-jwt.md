Q. What's a JWT ?

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