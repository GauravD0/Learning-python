#Error Handling in Python
#Error handling is a crucial aspect of programming that allows developers to manage and respond to runtime errors
#gracefully. In Python, error handling is primarily done using the try, except, else, and finally blocks.
#Example 1: Basic try and except
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#Example 2: Multiple except blocks
try:
    # Code that may raise different exceptions
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
#Example 3: Using else block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("The result is:", result)
#Example 4: Using finally block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("The result is:", result)
finally:
    print("Execution completed.")
