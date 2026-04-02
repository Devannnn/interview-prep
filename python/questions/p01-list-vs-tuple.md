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

