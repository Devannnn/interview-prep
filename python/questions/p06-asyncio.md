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