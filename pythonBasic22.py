#Tuples and sets in python
#Tuples are immutable sequences, typically used to store collections of heterogeneous data.
#Tuples are defined by enclosing the elements in parentheses ()
tuple1={"apple", 1, 5.0, True, "banana"}
print(tuple1)  # Output the entire tuple
tuple1[0] = "cherry" # This will raise an error because tuples are immutable
print(tuple1)  # Output the tuple after attempted modification

#sets in python
#Sets are unordered collections of unique elements.
#Sets are defined by enclosing the elements in curly braces {}
set1={1, 2, 3, 4, 5, 1, 2} # Duplicates will be removed
print(set1)  # Output the entire set