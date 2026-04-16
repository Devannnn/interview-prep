Q. What's a fixture in Pytest ?

A fixture is a setup function that Pytest calls before each test to provide a fresh resource (constants, database, app, etc).

The variable is injected at execution time by Pytest and the test access it like a normal parameter.

When the test ends, those ressources are torn down which ensure isolation between tests.

When you declare a fixture, you basically say "here's how to create the resource my test needs". That's how Pytest is able to create a fresh resource for each test.