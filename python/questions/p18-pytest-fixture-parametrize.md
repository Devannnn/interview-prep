Q. What's the different between fixtures and parametrized test in Pytest ?

Both of those concepts are used to give inputs to a test. But they solve two different problems :

- Fixtures provide a shared setup to the tests. They answer: "what environment does this test need?" and they ensure this environment is independent from others tests.

- Parametrize provides varied inputs that would be run on the same test logic. It answers: "which cases do my test cover?".

Another important distinction is that they're not evaluated at the same time.

Fixtures are evaluated at execution time.

Parametrized test are evaluated at collection time.

It's important because it explains why a parametrized decoractor accepts only plain Python values. If you give a fixture - or anything that is evaluated only at runtime - then it won't work.