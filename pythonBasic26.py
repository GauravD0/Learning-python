#For loops in python
#For loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
#The for loop in Python is more like a "for each" loop found in other programming
#languages, as it iterates over each item in the sequence.
#Example with a list
myList = [10, 20, 30, 40, 50]
for item in myList:
    print(item)  # Output each item in the list
#Example with a string
myString = "Hello"
for char in myString:
    print(char)  # Output each character in the string
#Example with a tuple
myTuple = (1, 2, 3, 4, 5)
for num in myTuple:
    print(num)  # Output each number in the tuple
#Example with a set
mySet = {100, 200, 300}
for value in mySet:
    print(value)  # Output each value in the set
#Example with a dictionary
myDict = {"a": 1, "b": 2, "c": 3}
for key in myDict:
    print(key, myDict[key])  # Output each key and its corresponding value
#Using range() with for loops
for i in range(5):
    print(i)  # Output numbers from 0 to 4
for i in range(2, 10, 2):
    print(i)  # Output even numbers from 2 to 8
#Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")  # Output pairs of i and j values
#Using else with for loops
for i in range(3):
    print(i)
else:
    print("Loop completed")  # Output after the loop finishes normally
#Using break and continue in for loops
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print(i)
#Using pass in for loops
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    print(i)
# Output each number from 0 to 4
