Q. What is the difference between args and kwargs? Write a function that accepts both and prints them.

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