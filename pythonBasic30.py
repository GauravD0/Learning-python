#inheritance in python
#Inheritance allows a class (child class) to inherit attributes and methods from another class (parent
#class). This promotes code reusability and establishes a relationship between classes.
#Defining the parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
#Defining the child class that inherits from the parent class
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class initializer
        self.breed = breed
    def speak(self):
        return f"{self.name} says meow!"
#Creating an object (instance) of the child class
my_cat = Cat("Whiskers", "Siamese")
#Accessing inherited attributes and methods
print(f"My cat's name is {my_cat.name} and she is a {my_cat.breed}.")
print(my_cat.speak())  # Call the overridden speak method
#Demonstrating polymorphism
def animal_sound(animal):
    print(animal.speak())
animal_sound(my_cat)  # Pass the Cat instance to the function
#You can also create another child class to demonstrate polymorphism
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
my_dog = Dog("Buddy")
animal_sound(my_dog)  # Pass the Dog instance to the function
print(f"My dog's name is {my_dog.name}.")
print(my_dog.speak())  # Call the Dog's speak method
#Using isinstance to check class relationships
print(isinstance(my_cat, Cat))      # True
print(isinstance(my_cat, Animal))   # True
print(isinstance(my_dog, Dog))      # True
print(isinstance(my_dog, Animal))   # True
print(isinstance(my_cat, Dog))      # False
#Using issubclass to check subclass relationships
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Animal))  # True
print(issubclass(Dog, Cat))     # False
#This code demonstrates the concept of inheritance in Python, including class definition,
#object creation, method overriding, polymorphism, and type checking using isinstance and issubclass
