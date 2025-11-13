#if else statements in python
# equals: a == b
# not equals: a != b
# greater than: a > b
# less than: a < b
# greater than or equal to: a >= b
# less than or equal to: a <= b
a= 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")    
#nested if else
x = 41 
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is not greater than 20")
else:
    print("x is not greater than 10")
#using and, or, not operators
c = 50
d = 30
if c > 20 and d < 40:
    print("Both conditions are true")
if c > 60 or d < 40:
    print("At least one condition is true")
if not c < 20:
    print("c is not less than 20")
#nested if with and, or
y = 25
if y > 10: 
    if y < 30 and y != 20:
        print("y is between 10 and 30 and not equal to 20")
    else:
        print("y is not between 10 and 30 or is equal to 20")
else:
    print("y is not greater than 10")
    