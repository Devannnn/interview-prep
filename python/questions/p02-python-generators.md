Q. What is a Python generator? Write a one-liner generator that yields squares of numbers from 1 to n.

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

