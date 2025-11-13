#python Dictionaries
#Dictionaries are mutable collections of key-value pairs.
#Dictionaries are defined by enclosing the elements in curly braces {} with key-value pairs separated by
#colons (:)
myDict = {"Name": "John", "Age": 30, "City": "New York"}
print(myDict)  # Output the entire dictionary
print(myDict["Name"])  # Output the value associated with the key "Name"
print(myDict.get("Age"))  # Output the value associated with the key "Age"
#various operations on dictionary
myDict["Age"] = 31  # Update the value associated with the key "Age"
print(myDict)  # Output the modified dictionary
myDict["Occupation"] = "Engineer"  # Add a new key-value pair
print(myDict)  # Output the modified dictionary
del myDict["City"]  # Remove the key-value pair with the key "City"
print(myDict)  # Output the modified dictionary
myDict.pop("Name")  # Remove the key-value pair with the key "Name"
print(myDict)  # Output the modified dictionary
