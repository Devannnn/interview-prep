Q. What's parametrization in Pytest ?

When testing an application, you might want to perform the same test on different inputs. For instance, you might check that a bunch of invalids requests are actually failing with an explicit error message. The naive way would be to write a test per input or to write one large tests with all the assertions but it would duplicate lot of code. 

The other solution is to use parametrization. It means to run the same test with different parameters. The test will be ran several times and each execution is independent.

In Pytest, you use a decoration called `@pytest.mark.parametrize`.