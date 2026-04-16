Q. What's `app.test_client()` for in Flask ?

`app.test_client` is a Flask method which return an object to simulate HTTP requests. This test client sends requests directly to the app without any server involved. It's used with fixtures to simulate client requests and assert that the API's response is correct. 

This feature allows to run test in isolation - thanks to the test client and its fixtures, each test receives a fresh state.

That's the standard way to test automatically application routes and allow to avoid running the application on a server and perform requests manually.
