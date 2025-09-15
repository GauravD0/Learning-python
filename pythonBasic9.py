#Global and Local Variables in Python
x = "I am Global"
def func():
    y = "I am Local"
    print(y)

print(x)

func()
print(y) #This will give error because y is local variable and can be used inside the function only