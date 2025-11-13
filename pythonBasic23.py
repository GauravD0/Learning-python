#sets in python
#Sets are unordered collections of unique elements.
#Sets are defined by enclosing the elements in curly braces {}
set1={1, 2, 3, 4, 5, 1, 2} # Duplicates will be removed
print(set1)  # Output the entire set
print(len(set1))  # Output the number of unique elements in the set
for f in set1:
    print(f)  # Output each element in the set
#operations on sets
set1.add(6)  # Add an element to the set
print(set1)  # Output the modified set
set1.remove(3)  # Remove an element from the set 
print(set1)  # Output the modified set
set1.discard(10)  # Remove an element if it exists, no error if
print(set1)  # Output the modified set
set1.pop()  # Remove and return an arbitrary element