# Python — interview questions

## Table of contents

- [1. What are the differences between a list, tuple, and set in Python? When would you choose one over the others?](#1-what-are-the-differences-between-a-list-tuple-and-set-in-python-when-would-you-choose-one-over-the-others)
- [2. What is the difference between mutable and immutable types in Python? Give examples of each.](#2-what-is-the-difference-between-mutable-and-immutable-types-in-python-give-examples-of-each)
- [3. What's the difference between `dict.get(key)` and `dict[key]`?](#3-whats-the-difference-between-dictgetkey-and-dictkey)
- [4. What's a comprehension in Python ?](#4-whats-a-comprehension-in-python)
- [5. What's the method `zip` for in Python ?](#5-whats-the-method-zip-for-in-python)
- [6. What's `if __name__ == "__main__"` for ?](#6-whats-if-name-main-for)
- [7. What's the difference between a module, a package and a library ?](#7-whats-the-difference-between-a-module-a-package-and-a-library)
- [8. What is the standard library in Python ?](#8-what-is-the-standard-library-in-python)
- [9. What's SQLite ?](#9-whats-sqlite)
- [10. What is the difference between a shallow copy and a deep copy?](#10-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy)
- [11. What's the different types of attributes in a class ?](#11-whats-the-different-types-of-attributes-in-a-class)
- [12. What's the difference between inheritance and composition ?](#12-whats-the-difference-between-inheritance-and-composition)
- [13. When would you define a custom exception class?](#13-when-would-you-define-a-custom-exception-class)
- [14. What is the difference between `else` and `finally` in a `try` statement?](#14-what-is-the-difference-between-else-and-finally-in-a-try-statement)
- [15. How do you handle errors properly in Python code?](#15-how-do-you-handle-errors-properly-in-python-code)
- [16. What is the difference between args and kwargs? Write a function that accepts both and prints them.](#16-what-is-the-difference-between-args-and-kwargs-write-a-function-that-accepts-both-and-prints-them)
- [17. Explain the difference between @staticmethod and @classmethod. When would you use each?](#17-explain-the-difference-between-staticmethod-and-classmethod-when-would-you-use-each)
- [18. What is a Python generator? Write a one-liner generator that yields squares of numbers from 1 to n.](#18-what-is-a-python-generator-write-a-one-liner-generator-that-yields-squares-of-numbers-from-1-to-n)
- [19. What's an ORM ? Can you name one drawback or risk of using an ORM?](#19-whats-an-orm-can-you-name-one-drawback-or-risk-of-using-an-orm)
- [20. What is the N+1 query problem in an ORM?](#20-what-is-the-n1-query-problem-in-an-orm)
- [21. What do black and isort do, and why do they need to be configured together?](#21-what-do-black-and-isort-do-and-why-do-they-need-to-be-configured-together)
- [22. What's a fixture in Pytest ?](#22-whats-a-fixture-in-pytest)
- [23. What's parametrization in Pytest ?](#23-whats-parametrization-in-pytest)
- [24. What's the different between fixtures and parametrized test in Pytest ?](#24-whats-the-different-between-fixtures-and-parametrized-test-in-pytest)
- [25. What's Pydantic ?](#25-whats-pydantic)
- [26. What's a decorator in Python ?](#26-whats-a-decorator-in-python)
- [27. When is Python a strong choice for a project, and when would you choose another language instead?](#27-when-is-python-a-strong-choice-for-a-project-and-when-would-you-choose-another-language-instead)
- [28. How would you store and validate a JSON schema for API results in Python ?](#28-how-would-you-store-and-validate-a-json-schema-for-api-results-in-python)
- [29. How do you write a unit test for a function that calls an external API, without actually hitting the API?](#29-how-do-you-write-a-unit-test-for-a-function-that-calls-an-external-api-without-actually-hitting-the-api)
- [30. Explain Python's `asyncio`. How does `async/await` differ from threading?](#30-explain-pythons-asyncio-how-does-asyncawait-differ-from-threading)
- [31. What is GIL in Python ?](#31-what-is-gil-in-python)
- [32. How do you achieve true parallelism in Python despite the GIL ?](#32-how-do-you-achieve-true-parallelism-in-python-despite-the-gil)
- [33. What does func(**some_dict) do in Python?](#33-what-does-funcsome-dict-do-in-python)

---
#### 1. What are the differences between a list, tuple, and set in Python? When would you choose one over the others?

<details>
<summary>Reveal answer</summary>

Lists, tuples and sets are all collections types in Python but they differ in ordering and mutability which make them useful for different usecases.

A list is an ordered, mutable collection of elements. It supports indexing.
my_list = [1,2,3]
I would use a list when I need a list of ordered elements that I can iterate on.

A tuple is an ordered immutable collection of elements. It supports indexing.
my_tuple = (1,2,3)
I would use a tuple when I need an immutable collection of elements. For instance, because I want to ensure data integrity.

A set is an unordered, mutable collection of unique elements. It doesn't support indexing.
my_set = {1,2,3}
I would use a set when I need fast membership check or when I need to remove duplicates.

</details>

---

#### 2. What is the difference between mutable and immutable types in Python? Give examples of each.

<details>
<summary>Reveal answer</summary>

A mutable object can be changed in place after it is created, like a `list`, `dict`, or `set`. An immutable object cannot be changed in place; operations create a new object instead. Examples include `tuple`, `str`, `int`, and `float`.

</details>

---

#### 3. What's the difference between `dict.get(key)` and `dict[key]`?

<details>
<summary>Reveal answer</summary>

Both are ways to retrieve the value associated to a key in a dictionnary.

The difference is how they handle missing keys.

The get method allows you to define a default value if the key is missing :

```jsx
dictionary.get("bogus", default_value)
```

and if no default value is provided, it returns None.

On the other hand, `dict[key]` raises a KeyError if the key is missing.

</details>

---

#### 4. What's a comprehension in Python ?

<details>
<summary>Reveal answer</summary>

A comprehension is a compact syntax to create collections from an iterable.

It's used to contain all the logic to create a collection in a single readable expression.

```python
# Instead of writing
result = []
for x in iterable:
    if condition(x):
        result.append(transform(x))

# You write
result = [transform(x) for x in iterable if condition(x)]
```

There is a comprehension for almost each type of collection: list, set, dict.

```python
[x for x in items]          # list comprehension

{x for x in items}          # set comprehension

{k: v for k, v in pairs}    # dict comprehension
```

</details>

---

#### 5. What's the method `zip` for in Python ?

<details>
<summary>Reveal answer</summary>

How I loop over several iterables at the same time ? With `zip`.

The `zip` takes several iterable and create a generator which pairs each element based on their index. It stops at the shortest iterable.

```python
names = ["Alice", "Bob", "Charlie", "Delta"]
scores = [90, 75, 88]
for name, score in zip(names, scores):
    print(name, score)
   
// Alice 90
// Bob 75
// Charlie 88
```

A cool usecase for zip is when you need to create a dictionnary out of several lists.

```python
names = ["Alice", "Bob", "Charlie", "Delta"]
scores = [90, 75, 88]
new_dict = dict(zip(names, scores))
// {'Alice': 90, 'Bob': 75, 'Charlie': 88}
```

</details>

---

#### 6. What's `if __name__ == "__main__"` for ?

<details>
<summary>Reveal answer</summary>

`__name__` is a variable managed by Python. When it runs a file directly, it sets this variable to `"__main__"` whereas when the same file is imported by another module, it sets this variable to the module's name.

Thanks to this, we can know if the curent script was directly executed or is merely imported. 

This is important because we don't want an imported module to execute code right away, we want it to merely expose methods that our code will then execute.

</details>

---

#### 7. What's the difference between a module, a package and a library ?

<details>
<summary>Reveal answer</summary>

A module is a single Python file `.py`.

A package is a folder containing several modules.

Modules and packages have a concrete meaning linked to the file structure. On the other hand, a library is more conceptual.

A library is a collection of reusable code designed to solve related problems. A library can be composed of one module, one package or several packages. The important part is that all of them provide functionnality around the same topic.

</details>

---

#### 8. What is the standard library in Python ?

<details>
<summary>Reveal answer</summary>

Python follows a philosophy called "batteries included" which mean that when you download an interpreter for python, it comes bundled with a collection of modules and packages called "the standard library".

The idea is that common tasks should be immediately available to users without them needing to download external packages.

Some examples of those standard libraries:

- `datetime` for dates and times manipulation
- `logging` for logs
- `unittest` for testing
- `json` for json manipulation
- `math` to get advanced math functions

Many believe that the success of Python is partly due to this philosophy. Developers can solve many everyday problems using reliable, built-in modules instead of reimplementing common functionality or immediately depending on external libraries.

</details>

---

#### 9. What's SQLite ?

<details>
<summary>Reveal answer</summary>

SQLite is a file-based relational database. It's convenient because unlike traditional database like MySQL, you don't need a separate server process nor installation.

That makes it the best choice if you need a fast way to persist data for local development.

However it lacks features needed in production like concurrent writing. That's why it's not recommended in production and is then replaced by a system like PostgreSQL.

</details>

---

#### 10. What is the difference between a shallow copy and a deep copy?

<details>
<summary>Reveal answer</summary>

Both are methods to make a copy of a Python object. The difference lays in the recursivity of the copy.

The copy method makes a shallow copy of the object. It creates a new object with a copy of all the top-level immutable items of the original object but still share the mutable items. It's basically a new container, with a references to the same nested objects.

A deepcopy makes a complete copy of the object meaning that it recursively copies all nested objects. It's basically a new container, with a copy of the nested objects.

A common bug is to use copy on an object with nested objects inside, thinking that you can now mutate the copy without modifying the original version. But because the copy contains references (and not duplicates) of the nested objects, it will actually modify also the original.

```python
a = {
    user : {
        name: "Test",
        age: 8
    }
}

b = a.copy()
b["user"]["age"] = 10
print(a["user"]["age"]) // returns 10
```

</details>

---

#### 11. What's the different types of attributes in a class ?

<details>
<summary>Reveal answer</summary>

There are two different types of attributes : instance attribute and class attribute.

Instance attributes are defined at the instance level and are stored in the instance. 

Class attributes are defined at the class level and are shared between instances. It's used to provide configuration and shared state across instances.

```python
class Car:
    working = False # Class attribute
    
    def __init__(self, name):
	    self.name = name # Instance attribute

clio = Car("clio")
tesla = Car("tesla")
```

A class attribute cannot be reassigned by the instance. If an instance tries to reassign a class attribute, it will create an instance attribute that shadows the class attribute *for this instance*.

```python
class Car:
    working = False # Class attribute
    
    def __init__(self, name):
	    self.name = name # Instance attribute

clio = Car("clio")
tesla = Car("tesla")

clio.working = True
print(clio.working) # True
print(tesla.working) # False
```

However, a class attribute can be *updated* at the class level. In that case, the attribute is modified for all instances. That's useful to create a shared state.


```python
class Car:
    counter = 0 # Class attribute
    
    def __init__(self, name):
	    self.name = name # Instance attribute
        Car.counter += 1

clio = Car("clio")
tesla = Car("tesla")

print(clio.counter)   # 2
print(tesla.counter)  # 2

```

</details>

---

#### 12. What's the difference between inheritance and composition ?

<details>
<summary>Reveal answer</summary>

Both are ways to reuse code.

Composition is when a class A is built using an instance of a class B, usually stored as an attribute, and delegates some work to it.

```python
// For example, let's say that you want to declare a UserService class that should 
// perform some task on behalf of the user. You want to be able to send an email.
// However, it makes no sense to make UserService inherites from EmailSender because
// it is not an email sender - it needs an email sender. Here, composition
// is the solution.

class UserService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def register_user(self, email):
        # create user in database
        self.email_sender.send_welcome_email(email)

// UserService has an instance of EmailSender as an attribute and delegate
// the sending of email to it.
```

</details>

---

#### 13. When would you define a custom exception class?

<details>
<summary>Reveal answer</summary>

A good practice is to define a custom exception when your application has a domain-specific error that you want to identify or handle separately.

You could raise a built-in exception for domain-specific errors - for example raise a ValueError for an invalid payment. It's not optimal though because many scenarios could lead to a ValueError exception and it could come from many places.

Whereas, if you define your own Exception - like InvalidPaymentError - you know right away what kind of error occurred and you can handle them separately.

</details>

---

#### 14. What is the difference between `else` and `finally` in a `try` statement?

<details>
<summary>Reveal answer</summary>

The `finally` block runs no matter what: whether the `try` block succeeds, raises an exception that is caught, or raises an exception that is not caught. It is usually used for cleanup, like closing files or releasing resources.

The `else` block runs only if the `try` block completes successfully without raising an exception. It is useful for code that should run only when no error occurred.

</details>

---

#### 15. How do you handle errors properly in Python code?

<details>
<summary>Reveal answer</summary>

I would put only the code that can fail inside the `try` block, then catch specific exceptions that I know how to handle. I would avoid a bare `except` because it can hide real bugs. In the `except` block, I would log the error, retry, use a fallback, or re-raise the exception depending on the situation. I would use `finally` for cleanup that must run whether the operation succeeds or fails.

</details>

---

#### 16. What is the difference between args and kwargs? Write a function that accepts both and prints them.

<details>
<summary>Reveal answer</summary>

To understand args and kwards, you must first understand positional and keyword arguments.

A positional argument is an argument passed based on its order in the function call.

A keyword argument is an argument passed based on the parameter name.

```python
def print_info(name, age):
    print(f'name : {name}, age : {age}')

print_info('fake_name', 20)
print_info(name='fake_name', age=20)
```

In Python, keywords arguments can only be placed after positional arguments.

Ok so what about *args and **kwargs ? Both are ways to retrieve additional parameters given to a function.

The difference is that args collects additional positional parameters in a tuple whereas kwargs collects additional keyword parameters in a dictionnary.

The names args and kwargs are conventions. What really matters are the symbols * and **.

```python
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(value)
```

</details>

---

#### 17. Explain the difference between @staticmethod and @classmethod. When would you use each?

<details>
<summary>Reveal answer</summary>

Class methods and static methods are specific types of methods in Python that are logically bound to a class rather than to its instances.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # This is an instance method
    def who(self):
        print(f"I am {self.name}")
    
    # This is a class method
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
    
    # This is  a static method
    @staticmethod
    def is_adult(age):
        return age >= 18
```

A class method is a method that receives the class itself as the first parameter - conventionally named cls. Those are often used to defined factory methods i.e. other ways to create an instance of that class.

In the example, we are using a class method to define a factory method in order to be able to create an instance of the class by giving the birthyear instead of the age.

A static method is a normal method which is put inside a class because it logically belongs there. You can see it as a helper. It does not interact with the class or the instance.

</details>

---

#### 18. What is a Python generator? Write a one-liner generator that yields squares of numbers from 1 to n.

<details>
<summary>Reveal answer</summary>

A generator is a type of iterator that produces elements lazily.

When you create a generator, you literally say to Python "here's how to produce the next element". You can
see it as a way to get a sequence of elements but instead of having the entire list stored in memory, you just tell Python
how to produce each element and it will gives them one at a time.

```python
def square_nums(n):
    for i in range(1,n+1):
        yield i*i
```

Notice that we don't use return like for a list but yield. You can read yield as "put this element next in the generator".

Generator are often used with comprehensions. The previous example would look like this :

```python
square_nums_generator = (i*i for i in range(1, n+1))
```

Then you would consume this generator like this :

```python
print(next square_nums_generator) # Literally print the next element of the generator
```

Or if you want to print the entire sequence :

```python
for num in square_nums_generator:
    print(num)
```

The purpose of generator is to give a memory-performant way to deal with large set of data. Generator are way more memory efficient than list. 

Look at those results for instance :

Memory before : 15.98 Mb
square_nums_list(1000000)
Memory after : 350 Mb

Memory before : 15.98 Mb
square_nums_generator(1000000)
Memory before : 15.99 Mb

How can that the performances be so different ?

The list computed and stored in memory 1 million elements. On the other hand, the generator almost didn't do anything. It's waiting for the user to get the next element.

This structure has one trade-off though which is that you can only iterate over it once. Once you exhausted a generator, subsequent iterations won't yield more values.

</details>

---

#### 19. What's an ORM ? Can you name one drawback or risk of using an ORM?

<details>
<summary>Reveal answer</summary>

An Object Relational Mapper, or ORM, is an abstraction used in software development to let application code interact with a relational database using entities instead of raw SQL. The idea is to represent database concepts with OOP: tables become classes, columns become attributes, and rows become instances.

The main advantage of an ORM is that it's natural to manipulate classes and instances in a code, whereas manipulating raw SQL is error-prone and requires to know about specific SQL syntax.

With an ORM, the actual SQL requests are built under the hood. They're also optimized for security. For instance, ORMs have in-built SQL injection protections that a code using raw SQL might lack.

The main drawback is that it hides the generated SQL. The SQL may be inefficient (N+1 queries problem), and this extra abstraction layer can make performance problems or debugging harder.s

</details>

---

#### 20. What is the N+1 query problem in an ORM?

<details>
<summary>Reveal answer</summary>

The N+1 query problem is often used to describe performance issues with ORM. It happens when the ORM performs one query to get a list of elements, then performs an additional query per element, hence resulting in N+1 queries.

For example, if you have a table Car and a table Wheel with a one-to-many relationship between the two tables then an ORM might do SELECT * FROM Car and then SELECT * FROM Wheel where [car.id](http://car.id/) = x.

Doing that many small queries is inefficient. It's often more efficient to do one complex query. That's because each round trips to the database is expensive.

Which means that you could get the same data in a much more efficient way if you were doing a more complex query such as a join.

</details>

---

#### 21. What do black and isort do, and why do they need to be configured together?

<details>
<summary>Reveal answer</summary>

`black` is a code formatter which rewrite Python files to enforce a consistent style. `isort` is a tool which reorder the imports of each file.

The purpose of those tools is to delete any discussions on the formatting. They ensure every file looks the same, regardless of who wrote it.

They should be configured together because they can conflict. Especially, `black` has some opinions on how imports should look. `isort` has others opinions. Without coordination between the two tools, they would reformat the same lines differently. To solve this, `isort` should be configured with `profile = "black"`.

</details>

---

#### 22. What's a fixture in Pytest ?

<details>
<summary>Reveal answer</summary>

A fixture is a setup function that Pytest calls before each test to provide a fresh resource (constants, database, app, etc).

The variable is injected at execution time by Pytest and the test access it like a normal parameter.

When the test ends, those ressources are torn down which ensure isolation between tests.

When you declare a fixture, you basically say "here's how to create the resource my test needs". That's how Pytest is able to create a fresh resource for each test.

</details>

---

#### 23. What's parametrization in Pytest ?

<details>
<summary>Reveal answer</summary>

When testing an application, you might want to perform the same test on different inputs. For instance, you might check that a bunch of invalids requests are actually failing with an explicit error message. The naive way would be to write a test per input or to write one large tests with all the assertions but it would duplicate lot of code. 

The other solution is to use parametrization. It means to run the same test with different parameters. The test will be ran several times and each execution is independent.

In Pytest, you use a decoration called `@pytest.mark.parametrize`.

</details>

---

#### 24. What's the different between fixtures and parametrized test in Pytest ?

<details>
<summary>Reveal answer</summary>

Both of those concepts are used to give inputs to a test. But they solve two different problems :

- Fixtures provide a shared setup to the tests. They answer: "what environment does this test need?" and they ensure this environment is independent from others tests.

- Parametrize provides varied inputs that would be run on the same test logic. It answers: "which cases do my test cover?".

Another important distinction is that they're not evaluated at the same time.

Fixtures are evaluated at execution time.

Parametrized test are evaluated at collection time.

It's important because it explains why a parametrized decoractor accepts only plain Python values. If you give a fixture - or anything that is evaluated only at runtime - then it won't work.

</details>

---

#### 25. What's Pydantic ?

<details>
<summary>Reveal answer</summary>

Pydantic is a Python library used to validate data against a schema. It's often used to check that data sent by a user before persisting it in the database.

The schema declares what the API accepts.

The model declares what the database stores.

Those two are separated because they can evolve independently - you might want to have fewer fields expose on the API that what you actually store into the database.

</details>

---

#### 26. What's a decorator in Python ?

<details>
<summary>Reveal answer</summary>

A decorator is a function that takes another function as input and returns a new function, usually a wrapper. It lets us add behavior around the original function without changing its internal code. Common use cases include validating parameters, logging, measuring execution time, caching results, authentication, or rate limiting.

</details>

---

#### 27. When is Python a strong choice for a project, and when would you choose another language instead?

<details>
<summary>Reveal answer</summary>

Python is a strong choice for projects that benefit from readability, fast development, a large ecosystem, and a strong community, such as automation, APIs, data analysis, and prototyping. I would choose another language when the project has strict performance, memory, real-time, or system-level constraints.

</details>

---

#### 28. How would you store and validate a JSON schema for API results in Python ?

<details>
<summary>Reveal answer</summary>

I would define a JSON schema to describe the expected result and validate incoming data using an external library like `json-schema` or `pydantic`.

</details>

---

#### 29. How do you write a unit test for a function that calls an external API, without actually hitting the API?

<details>
<summary>Reveal answer</summary>

I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.

</details>

---

#### 30. Explain Python's `asyncio`. How does `async/await` differ from threading?

<details>
<summary>Reveal answer</summary>

asyncio is a Python library to write concurrent code using asynchronous programming. It's using an event loop that schedules and executes tasks cooperatively using async and await.

By default, a Python code is synchronous which means that operations run sequentially : an instruction will be ran only when the previous instructions are done.

But, there are scenarios where we have instructions that take time to perform because they are waiting for something - a network request, a database request, a file manipulation, etc - and we could perform other tasks meanwhile. Those type of instructions are called I/O-bound operations. Literally those are operations with plenty of time spent waiting. When you run those operations in a synchronous program, you lose lot of time doing nothing.

That's what asynchronous programming is for. It's a tool to write this efficient, non-blocking code.

Here's an example :

```python
import time
import asyncio
from typing import List, Dict

async def process_order(order_id: int, processing_time: float) -> Dict:
    # Simulate processing a single order.
    print(f'Starting to process order {order_id}')
    await asyncio.sleep(processing_time)  # Simulate I/O work (e.g., database/API calls)
    print(f'Finished processing order {order_id}')
    return {
    'order_id': order_id,
    'status': 'completed',
    'processing_time': processing_time
    }

    async def process_orders(orders: List[Dict]) -> List[Dict]:
    # Process multiple orders concurrently.
    tasks = [
    process_order(order['id'], order['processing_time'])
    for order in orders
    ]
    return await asyncio.gather(*tasks)

async def main():
    # Simulate different orders with varying processing times
    orders = [
        {'id': 1, 'processing_time': 2},  # Takes 2 seconds
        {'id': 2, 'processing_time': 1},  # Takes 1 second
        {'id': 3, 'processing_time': 3},  # Takes 3 seconds
    ]

    print('Starting order processing...')
    start_time = time.time()

    results = await process_orders(orders)

    end_time = time.time()
    total_time = end_time - start_time

    print(f'\nProcessed {len(results)} orders in {total_time:.2f} seconds')
    print(f'Individual results: {results}')
```

Now what's the difference with multi-threading ?

Asynchronous programming and multithreading are two ways to run concurrent tasks.

The main difference is that asyncio allows to have concurrency without parallelism. With asyncio, all tasks are run in the same thread. Each task explicitely gives up control - using await - allowing the event loop to switch tasks (hence the term cooperative). On the other hand, multithreading uses several threads to run tasks concurrently. A task itself doesn't decide whereas it executes or not : the OS scheduler decides which thread to run and interrupt the others meanwhile.

When to use asyncio over multi-threading ? For non-blocking I/O-bound operations. An I/O-bound operation is an operation where you wait most of the time (a request for instance). In that case, it's easy to see that you could keep executing tasks while waiting for the answer. You could use also thread but it adds the overhead of threads and context-switching.

When to use multi-threading over asyncio ? For blocking code. For instance, the requests library was built for synchronous programming. Hence, requests.get() never yields control. It blocks the programm until response arrives.

</details>

---

#### 31. What is GIL in Python ?

<details>
<summary>Reveal answer</summary>

Python's Global Interpret Lock (GIL) is a mutex that prevents multiple threads from executing Python bytecode simultaneously. It means that even if it seems that your code is running with multiple threads, only one thread at a time actually run the bytecode.

It means Python threads don't achieve true parallelism for CPU-bound tasks.

It doesn't mean that multithreading won't improve performance though. Many scenarios require blocking I/O-bound tasks where the thread spend most of the time waiting for an answer. No need to actually run the Python code.

The implementation of Python used matters here. The default Python implementation - and most widely used - is CPython, and that's the one with the GIL. It's an example of design tradeoff. Implementing the GIL made the rest of the implementation easier but reduced the capabilities. The main advantage of GIL being the memory management is simpler because you don't have to manage fine-grain locks to access ressources.

Others implementations of Python like Jython don't have this limitation but comes with others tradeoffs.

</details>

---

#### 32. How do you achieve true parallelism in Python despite the GIL ?

<details>
<summary>Reveal answer</summary>

If you use CPython, you can obtain true parallelism onmy if you use separate CPython interpreter. In practice, it means using different processes (and not just threads) as each one of them would have its own CPython interpreter and its own GIL.

</details>

---

#### 33. What does func(**some_dict) do in Python?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>


---
