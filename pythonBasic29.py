#classes in python
#A class is a blueprint for creating objects. It defines a set of attributes and methods that
#the created objects will have.
#Defining a class
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def bark(self):
        return f"{self.name} says woof!"
#Creating an object (instance) of the class
my_dog = Dog("Buddy", 3)
#Accessing class attributes and methods
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(my_dog.bark())  # Call the bark method
