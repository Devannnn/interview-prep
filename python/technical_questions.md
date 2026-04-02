# Explain the difference between @staticmethod and @classmethod. When would you use each?
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



# What is a Python generator? Write a one-liner generator that yields squares of numbers from 1 to n.
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



# What are the differences between a list, tuple, and set in Python? When would you choose one over the others?
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



# What is the difference between deepcopy and copy? Give a scenario where using copy would cause a bug.
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



# How would you store and validate a JSON schema for API results in Python ?

I would define a JSON schema to describe the expected result and validate incoming data using an external library like `json-schema` or `pydantic`.



# What is the difference between args and kwargs? Write a function that accepts both and prints them.
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



# How do you write a unit test for a function that calls an external API, without actually hitting the API?
I would mock the API request so it returns a predefined response. That way, the function can be tested in isolation without hitting the real API. This can be done using the library `pytest` for instance.



# What is the difference between localStorage, sessionStorage, and cookies?
Localstorage, sessionStorage and cookies are all ways to store user-specific data to provide a more custom experience.

LocalStorage is a local storage for your browser. It stores data permanently which means those data are persisted between page reloads and browser restarts. It can save as much as 10 Mb. It's not cleared automatically - the cache needs to be cleared. Only the client-side reads this storage.

SessionStorage stores data temporarily, until you close the tab or the window. It's a bit smaller - 5 Mb. Only the client-side reads this storage.

Cookies are very tiny data - 4 Kb - stored in the browser and which are sent to the server at each HTTP request.



# What is CORS and how would you configure it correctly for a Python backend serving a frontend on a different domain?
To understand CORS, you first need to understand same-origin policy (SOP).

SOP is a security mechanism on the browser. The principle is simple : let's say you got unlucky and opened a malicious website whose domain is `http://evil.com`. This website ran a malicious script into your browser. Bad news, it already has access to your local storage, session storage and cookies... BUT those are only data related to the page it opened. What the attacker would like is to get access to any site in your browser (bank, social networks, email, etc). For this, it sends a request to those sites - e.g `bank.com` - and reads the response. 

That's where SOP plays its role. SOP prevents script running in one origin (protocol + domain + port) from reading data from another origin. 

Here, it means that the browser doesn't allow the malicious script running at `http://evil.com` from reading data coming from `http://bank.com`. SOP doesn't prevent from sending the request, but it prevents the frontend from reading the response.

Without SOP, an attacker could read any site in your browser after you opened just one malicious tab. This would be catastrophic.

SOP is useful but it becomes a problem when you are developing a frontend and a backend with different domains. For instance, `https://frontend.example.com` and `https://api.example.com`. Here, the browser won't allow your frontend to see the data sent by your backend.

The solution is to configure the mechanism that manages the interactions between different domains : cross-origin resource sharing or CORS.

It's a security mechanism implemented by browsers to control which domains can access resources from a different origin. By default, it applies the same-origin policy.

The solution is to configure CORS in the backend to define which origins are allowed to fetch resources.

In Flask, it would be :
```
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://frontend.example.com"])
```

This tells the browser that requests from ``https://frontend.example.com`` are allowed to read the responses from your API.



# Explain Python's `asyncio`. How does `async/await` differ from threading? 
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


# What is GIL in Python ?
Python’s Global Interpret Lock (GIL) is a mutex that prevents multiple threads from executing Python bytecode simultaneously. It means that even if it seems that your code is running with multiple threads, only one thread at a time actually run the bytecode.

It means Python threads don’t achieve true parallelism for CPU-bound tasks.

It doesn’t mean that multithreading won’t improve performance though. Many scenarios require blocking I/O-bound tasks where the thread spend most of the time waiting for an answer. No need to actually run the Python code.

The implementation of Python used matters here. The default Python implementation - and most widely used - is CPython, and that’s the one with the GIL. It’s an example of design tradeoff. Implementing the GIL made the rest of the implementation easier but reduced the capabilities. The main advantage of GIL being the memory management is simpler because you don’t have to manage fine-grain locks to access ressources.

Others implementations of Python like Jython don’t have this limitation but comes with others tradeoffs.



# How do you achieve true parallelism in Python despite the GIL ?
If you use CPython, you can obtain true parallelism onmy if you use separate CPython interpreter. In practice, it means using different processes (and not just threads) as each one of them would have its own CPython interpreter and its own GIL.



# What’s CPU-bound and I/O-bound tasks ?
The term X-bound designates a type of task which is limited by a specific ressource. It means this task is spending most of its time using that ressource and that its performance depends on the ressource’s access.

A CPU-bound task means that this task spends most of its time executing instructions on the CPU - for instance a program computing the decimals of pi. The CPU’s performance is the main bottleneck for this task. You improve the performance of a CPU-bound task by using multi-processing.

An I/O-bound task means that this task spends most its time waiting for external operations such as network, database or disk access. In that example, the disk’s performance is the main bottleneck for this task. You improve the performance of an I/O-bound task by using concurrency to keep executing operations during the waiting time.





