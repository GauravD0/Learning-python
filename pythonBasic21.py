#Python List
#List are stored in squared brackets
#List can store multiple data types
#List are mutable, meaning they can be changed later on 
myList = [1, 2, 3, 4, 5, "Hello", True, 3.14]
print(myList)  # Output the entire list
print(myList[0])  # Output the first element
print(myList[-2]) # Output the second last element
print(myList[1:4])  # Output elements from index 1 to 3
# Output a slice of the list
print(myList[2:])  # Output elements from index 2 to the end
# Output elements from index 2 to the end
print(myList[:3])  # Output elements from the start to index 2
#various operations on list
myList.append("New Item")  # Add an item to the end of the list
print(myList)  # Output the modified list
myList.insert(2, "Inserted Item")  # Insert an item at index 2
print(myList)  # Output the modified list
myList.remove(3.14)  # Remove the first occurrence of 3.14
print(myList)  # Output the modified list
myList.pop()  # Remove the last item
print(myList)  # Output the modified list
# Python List Operations
print(len(myList))  # Output the length of the list
print(myList.count(1))  # Count occurrences of 1
print(myList.index("Hello"))  # Find the index of "Hello"
#myList.sort()  # Sort the list in ascending order
print(myList)  # Output the sorted list
myList.reverse()  # Reverse the list
print(myList)  # Output the reversed list
myList.clear()  # Clear the list
print(myList)  # Output the cleared list
