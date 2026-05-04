# Python — interview questions

## Table of contents

- [1. What are the differences between a list, tuple, and set in Python? When would you choose one over the others?](#1-what-are-the-differences-between-a-list-tuple-and-set-in-python-when-would-you-choose-one-over-the-others)
- [2. What is a Python generator? Write a one-liner generator that yields squares of numbers from 1 to n.](#2-what-is-a-python-generator-write-a-one-liner-generator-that-yields-squares-of-numbers-from-1-to-n)
- [3. What is the difference between a shallow copy and a deep copy?](#3-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy)
- [4. Explain the difference between @staticmethod and @classmethod. When would you use each?](#4-explain-the-difference-between-staticmethod-and-classmethod-when-would-you-use-each)
- [5. What is the difference between args and kwargs? Write a function that accepts both and prints them.](#5-what-is-the-difference-between-args-and-kwargs-write-a-function-that-accepts-both-and-prints-them)
- [6. Explain Python's `asyncio`. How does `async/await` differ from threading?](#6-explain-pythons-asyncio-how-does-asyncawait-differ-from-threading)
- [7. What is GIL in Python ?](#7-what-is-gil-in-python)
- [8. How do you achieve true parallelism in Python despite the GIL ?](#8-how-do-you-achieve-true-parallelism-in-python-despite-the-gil)
- [9. How would you store and validate a JSON schema for API results in Python ?](#9-how-would-you-store-and-validate-a-json-schema-for-api-results-in-python)
- [10. How do you write a unit test for a function that calls an external API, without actually hitting the API?](#10-how-do-you-write-a-unit-test-for-a-function-that-calls-an-external-api-without-actually-hitting-the-api)
- [11. What's `if __name__ == "__main__"` for ?](#11-whats-if-name-main-for)
- [12. What's an ORM ?](#12-whats-an-orm)
- [13. What's SQLite ?](#13-whats-sqlite)
- [14. What do black and isort do, and why do they need to be configured together?](#14-what-do-black-and-isort-do-and-why-do-they-need-to-be-configured-together)
- [15. What's a fixture in Pytest ?](#15-whats-a-fixture-in-pytest)
- [16. What's parametrization in Pytest ?](#16-whats-parametrization-in-pytest)
- [17. What's the different between fixtures and parametrized test in Pytest ?](#17-whats-the-different-between-fixtures-and-parametrized-test-in-pytest)
- [18. What's Pydantic ?](#18-whats-pydantic)
- [19. What does func(**some_dict) do in Python?](#19-what-does-funcsome-dict-do-in-python)
- [20. What's a decorator in Python ?](#20-whats-a-decorator-in-python)
- [21. What's the difference between *args and **kwargs ?](#21-whats-the-difference-between-args-and-kwargs)

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

#### 2. What is a Python generator? Write a one-liner generator that yields squares of numbers from 1 to n.

<details>
<summary>Reveal answer</summary>

A generator is a type of iterator that produces elements lazily.

When you create a generator, you literally say to Python "here's how to produce the next element". You can
see it as a way to get a sequence of elements but instead of having the entire list stored in memory, you just tell Python
how to produce each element and it will gives them one at a time.

def square_nums(n):
    for i in range(1,n+1):
        yield i*i

Notice that we don't use return like for a list but yield. You can read yield as "put this element next in the generator".

Generator are often used with comprehensions. The previous example would look like this :
square_nums_generator = (i*i for i in range(1, n+1))

Then you would consume this generator like this :
print(next square_nums_generator) # Literally print the next element of the generator

Or if you want to print the entire sequence :
for num in square_nums_generator:
    print(num)

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

#### 3. What is the difference between a shallow copy and a deep copy?

<details>
<summary>Reveal answer</summary>

Both are methods to make a copy of a Python object. The difference lays in the recursivity of the copy.

The copy method makes a shallow copy of the object. It creates a new object with a copy of all the top-level immutable items of the original object but still share the mutable items. It's basically a new container, with a references to the same nested objects.

A deepcopy makes a complete copy of the object meaning that it recursively copies all nested objects. It's basically a new container, with a copy of the nested objects.

A common bug is to use copy on an object with nested objects inside, thinking that you can now mutate the copy without modifying the original version. But because the copy contains references (and not duplicates) of the nested objects, it will actually modify also the original.

a = {
    user : {
        name: "Test",
        age: 8
    }
}

b = a.copy()
b["user"]["age"] = 10
print(a["user"]["age"]) // returns 10

</details>

---

#### 4. Explain the difference between @staticmethod and @classmethod. When would you use each?

<details>
<summary>Reveal answer</summary>

Class methods and static methods are specific types of methods in Python that are logically bound to a class rather than to its instances.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

A class method is a method that receives the class itself as the first parameter - conventionally named cls. Those are often used to defined factory methods i.e. other ways to create an instance of that class.

In the example, we are using a class method to define a factory method in order to be able to create an instance of the class by giving the birthyear instead of the age.

A static method is a normal method which is put inside a class because it logically belongs there. You can see it as a helper. It does not interact with the class or the instance.

</details>

---

#### 5. What is the difference between args and kwargs? Write a function that accepts both and prints them.

<details>
<summary>Reveal answer</summary>

To understand args and kwards, you must first understand positional and keyword arguments.

A positional argument is an argument passed based on its order in the function call.

A keyword argument is an argument passed based on the parameter name.

def print_info(name, age):
    print(f'name : {name}, age : {age}')

print_info('fake_name', 20)
print_info(name='fake_name', age=20)

In Python, keywords arguments can only be placed after positional arguments.

Ok so what about *args and **kwargs ? Both are ways to retrieve additional parameters given to a function.

The difference is that args collects additional positional parameters in a tuple whereas kwargs collects additional keyword parameters in a dictionnary.

The names args and kwargs are conventions. What really matters are the symbols * and **.

def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(value)

</details>

---

#### 6. Explain Python's `asyncio`. How does `async/await` differ from threading?

<details>
<summary>Reveal answer</summary>

asyncio is a Python library to write concurrent code using asynchronous programming. It's using an event loop that schedules and executes tasks cooperatively using async and await.

By default, a Python code is synchronous which means that operations run sequentially : an instruction will be ran only when the previous instructions are done.

But, there are scenarios where we have instructions that take time to perform because they are waiting for something - a network request, a database request, a file manipulation, etc - and we could perform other tasks meanwhile. Those type of instructions are called I/O-bound operations. Literally those are operations with plenty of time spent waiting. When you run those operations in a synchronous program, you lose lot of time doing nothing.

That's what asynchronous programming is for. It's a tool to write this efficient, non-blocking code.

Here's an example :
import time
import asyncio
from typing import List, Dict

async def process_order(order_id: int, processing_time: float) -> Dict:
'''Simulate processing a single order.'''
print(f'Starting to process order {order_id}')
await asyncio.sleep(processing_time)  # Simulate I/O work (e.g., database/API calls)
print(f'Finished processing order {order_id}')
return {
'order_id': order_id,
'status': 'completed',
'processing_time': processing_time
}

async def process_orders(orders: List[Dict]) -> List[Dict]:
'''Process multiple orders concurrently.'''
tasks = [
process_order(order['id'], order['processing_time'])
for order in orders
]
return await asyncio.gather(*tasks)

async def main():

```
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

print(f'\\nProcessed {len(results)} orders in {total_time:.2f} seconds')
print(f'Individual results: {results}')
```

Now what's the difference with multi-threading ?

Asynchronous programming and multithreading are two ways to run concurrent tasks.

The main difference is that asyncio allows to have concurrency without parallelism. With asyncio, all tasks are run in the same thread. Each task explicitely gives up control - using await - allowing the event loop to switch tasks (hence the term cooperative). On the other hand, multithreading uses several threads to run tasks concurrently. A task itself doesn't decide whereas it executes or not : the OS scheduler decides which thread to run and interrupt the others meanwhile.

When to use asyncio over multi-threading ? For non-blocking I/O-bound operations. An I/O-bound operation is an operation where you wait most of the time (a request for instance). In that case, it's easy to see that you could keep executing tasks while waiting for the answer. You could use also thread but it adds the overhead of threads and context-switching.

When to use multi-threading over asyncio ? For blocking code. For instance, the requests library was built for synchronous programming. Hence, requests.get() never yields control. It blocks the programm until response arrives.

</details>

---

#### 7. What is GIL in Python ?

<details>
<summary>Reveal answer</summary>

Python’s Global Interpret Lock (GIL) is a mutex that prevents multiple threads from executing Python bytecode simultaneously. It means that even if it seems that your code is running with multiple threads, only one thread at a time actually run the bytecode.

It means Python threads don’t achieve true parallelism for CPU-bound tasks.

It doesn’t mean that multithreading won’t improve performance though. Many scenarios require blocking I/O-bound tasks where the thread spend most of the time waiting for an answer. No need to actually run the Python code.

The implementation of Python used matters here. The default Python implementation - and most widely used - is CPython, and that’s the one with the GIL. It’s an example of design tradeoff. Implementing the GIL made the rest of the implementation easier but reduced the capabilities. The main advantage of GIL being the memory management is simpler because you don’t have to manage fine-grain locks to access ressources.

Others implementations of Python like Jython don’t have this limitation but comes with others tradeoffs.

</details>

---

#### 8. How do you achieve true parallelism in Python despite the GIL ?

<details>
<summary>Reveal answer</summary>

If you use CPython, you can obtain true parallelism onmy if you use separate CPython interpreter. In practice, it means using different processes (and not just threads) as each one of them would have its own CPython interpreter and its own GIL.

</details>

---

#### 9. How would you store and validate a JSON schema for API results in Python ?

<details>
<summary>Reveal answer</summary>

I would define a JSON schema to describe the expected result and validate incoming data using an external library like `json-schema` or `pydantic`.

</details>

---

#### 10. How do you write a unit test for a function that calls an external API, without actually hitting the API?

<details>
<summary>Reveal answer</summary>

I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.

</details>

---

#### 11. What's `if __name__ == "__main__"` for ?

<details>
<summary>Reveal answer</summary>

`__name__` is a variable managed by Python. When it runs a file directly, it sets this variable to `"__main__"` whereas when the same file is imported by another module, it sets this variable to the module's name.

Thanks to this, we can know if the curent script was directly executed or is merely imported. 

This is important because we don't want an imported module to execute code right away, we want it to merely expose methods that our code will then execute.

</details>

---

#### 12. What's an ORM ?

<details>
<summary>Reveal answer</summary>

An ORM or Object Relational Mapper is a library that allows a code to interact with a database by manipulating entities instead of using raw SQL.

In an ORM, each table is represented as a class and each column is represented as a field.

The main advantage of an ORM is that it's natural to manipulate classes and instances in a code, whereas manipulating raw SQL is error-prone and requires to know about specific SQL syntax.

With an ORM, the actual SQL requests are built under the hood. They're also optimized for performance and security. For instance, ORMs have in-built SQL injection protections that a code using raw SQL might lack.

</details>

---

#### 13. What's SQLite ?

<details>
<summary>Reveal answer</summary>

SQLite is a file-based relational database. It's convenient because unlike traditional database like MySQL, you don't need a separate server process nor installation.

That makes it the best choice if you need a fast way to persist data for local development.

However it lacks features needed in production like concurrent writing. That's why it's not recommended in production and is then replaced by a system like PostgreSQL.

</details>

---

#### 14. What do black and isort do, and why do they need to be configured together?

<details>
<summary>Reveal answer</summary>

`black` is a code formatter which rewrite Python files to enforce a consistent style. `isort` is a tool which reorder the imports of each file.

The purpose of those tools is to delete any discussions on the formatting. They ensure every file looks the same, regardless of who wrote it.

They should be configured together because they can conflict. Especially, `black` has some opinions on how imports should look. `isort` has others opinions. Without coordination between the two tools, they would reformat the same lines differently. To solve this, `isort` should be configured with `profile = "black"`.

</details>

---

#### 15. What's a fixture in Pytest ?

<details>
<summary>Reveal answer</summary>

A fixture is a setup function that Pytest calls before each test to provide a fresh resource (constants, database, app, etc).

The variable is injected at execution time by Pytest and the test access it like a normal parameter.

When the test ends, those ressources are torn down which ensure isolation between tests.

When you declare a fixture, you basically say "here's how to create the resource my test needs". That's how Pytest is able to create a fresh resource for each test.

</details>

---

#### 16. What's parametrization in Pytest ?

<details>
<summary>Reveal answer</summary>

When testing an application, you might want to perform the same test on different inputs. For instance, you might check that a bunch of invalids requests are actually failing with an explicit error message. The naive way would be to write a test per input or to write one large tests with all the assertions but it would duplicate lot of code. 

The other solution is to use parametrization. It means to run the same test with different parameters. The test will be ran several times and each execution is independent.

In Pytest, you use a decoration called `@pytest.mark.parametrize`.

</details>

---

#### 17. What's the different between fixtures and parametrized test in Pytest ?

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

#### 18. What's Pydantic ?

<details>
<summary>Reveal answer</summary>

Pydantic is a Python library used to validate data against a schema. It's often used to check that data sent by a user before persisting it in the database.

The schema declares what the API accepts.

The model declares what the database stores.

Those two are separated because they can evolve independently - you might want to have fewer fields expose on the API that what you actually store into the database.

</details>

---

#### 19. What does func(**some_dict) do in Python?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 20. What's a decorator in Python ?

<details>
<summary>Reveal answer</summary>

- you can combine decorator, order matters then

</details>

---

#### 21. What's the difference between *args and **kwargs ?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---
