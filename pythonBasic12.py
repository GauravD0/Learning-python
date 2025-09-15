#There are various functions of strings in python like
#indexing we can do indexing of strings like this
x = "Gaurav"
print(x[3]) #it will print r because indexes starts from 0

#Another Function is string length
#to find the length we use len() function
print(len(x)) #it will print the length of the string which is 6

#Another function is slicing of string to do this will put the indexes in square brackets like
#x[start:end] here start is inclusive and end is exclusive
print(x[1:4]) #it will print aur because 1 is inclusive and 4 is exclusive

#to start from default index we can leave it blank 
print(x[:4]) #it will print Gaur because it will start from 0 index

#same goes for end index also 
print(x[1:]) #it will print aurav because it will go till the last index