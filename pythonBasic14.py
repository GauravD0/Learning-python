x = "Gaurav"
y = "Deshmukh"

z= f"{x} {y}"
print(z) #this will print the strings combined with spaces by using fstring 

#we can also do this with the help of format() function
age = 21 #we can also add other data types like integer also
w = "{} {} is {} years old".format(x, y, age)
print(w) #this will print the string combined with spaces by using format() function