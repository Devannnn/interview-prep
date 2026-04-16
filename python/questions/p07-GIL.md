Q. What is GIL in Python ?

Python’s Global Interpret Lock (GIL) is a mutex that prevents multiple threads from executing Python bytecode simultaneously. It means that even if it seems that your code is running with multiple threads, only one thread at a time actually run the bytecode.

It means Python threads don’t achieve true parallelism for CPU-bound tasks.

It doesn’t mean that multithreading won’t improve performance though. Many scenarios require blocking I/O-bound tasks where the thread spend most of the time waiting for an answer. No need to actually run the Python code.

The implementation of Python used matters here. The default Python implementation - and most widely used - is CPython, and that’s the one with the GIL. It’s an example of design tradeoff. Implementing the GIL made the rest of the implementation easier but reduced the capabilities. The main advantage of GIL being the memory management is simpler because you don’t have to manage fine-grain locks to access ressources.

Others implementations of Python like Jython don’t have this limitation but comes with others tradeoffs.