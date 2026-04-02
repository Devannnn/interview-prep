# How do you write a unit test for a function that calls an external API, without actually hitting the API?

I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.