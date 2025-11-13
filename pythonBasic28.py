#Functions in python
#Functions are defined using the def keyword followed by the function name and parentheses ()
def greet(name):
    """This function greets the person passed as a parameter."""
    print("Hello, " + name + "!")
greet("Alice")  # Call the function with the argument "Alice"
#Function with return value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b
result = add(5, 3)  # Call the function and store the result
print("The sum is:", result)  # Output the result
#Function with default parameter
def power(base, exponent=2):
    """This function returns the base raised to the exponent."""
    return base ** exponent
print("2 to the power of 3 is:", power(2, 3))  # Call with both parameters
print("3 squared is:", power(3))  # Call with default exponent
#Function with variable-length arguments
def multiply(*args):
    """This function returns the product of all arguments."""
    product = 1
    for num in args:
        product *= num
    return product
print("Product of 2, 3, 4 is:", multiply(2, 3, 4))  # Call with multiple arguments
#Function with keyword arguments
def introduce(**kwargs):
    """This function introduces a person using keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
introduce(name="Bob", age=30, city="New York")  # Call with keyword arguments
#Lambda function (anonymous function)
square = lambda x: x * x
print("Square of 5 is:", square(5))  # Call the lambda function
#Using functions as arguments
def apply_function(func, value):
    """This function applies a given function to a value."""
    return func(value)
print("Applying square function to 6:", apply_function(square, 6))  # Pass lambda function as argument
#Nested functions
def outer_function(msg):
    """This function contains a nested function."""
    def inner_function():
        print("Message from inner function:", msg)
    inner_function()  # Call the nested function
outer_function("Hello from outer function!")  # Call the outer function
#Recursion example
def factorial(n):
    """This function returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))  # Call the recursive function
#Function annotations
def annotated_function(x: int, y: int) -> int:
    """This function adds two integers and returns an integer."""
    return x + y
print("Annotated function result:", annotated_function(10, 20))  # Call the annotated function
#Output the function's annotations
print("Function annotations:", annotated_function.__annotations__)
