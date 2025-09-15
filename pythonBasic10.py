#we can change the value of global variable inside a function by using 'global' keyword
x = "I am Global"

def func():
    global x #using global keyword
    x= "I am changed"
    print(x)

print(x)
func()
print(x) #here the value has been changed because we used 'global' keyword inside the function