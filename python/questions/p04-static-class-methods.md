Q. Explain the difference between @staticmethod and @classmethod. When would you use each?

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