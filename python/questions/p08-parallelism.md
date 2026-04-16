Q. How do you achieve true parallelism in Python despite the GIL ?

If you use CPython, you can obtain true parallelism onmy if you use separate CPython interpreter. In practice, it means using different processes (and not just threads) as each one of them would have its own CPython interpreter and its own GIL.