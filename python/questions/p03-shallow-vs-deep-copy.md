Q. What is the difference between a shallow copy and a deep copy?

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