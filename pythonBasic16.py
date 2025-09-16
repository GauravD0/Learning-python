#other string methods are
#isdigit() function to check whether the string is digit or not
x = "1234"
print(x.isdigit()) #it will return True because the string contains only digits

#isalpha() function to check whether the string contains only alphabets or not
y = "Gaurav"
print(y.isalpha()) #it will return True because the string contains only alphabets
z = "Gaurav123"
print(z.isalpha()) #it will return False because the string contains digits also
#isalnum() function to check whether the string contains only alphabets and digits or not
a = "Gaurav123"
print(a.isalnum()) #it will return True because the string contains only alphabets and digits
b = "Gaurav@123"
print(b.isalnum()) #it will return False because the string contains special characters also
#endswith() function to check whether the string ends with the given substring or not
c = "Gaurav" 
print(c.endswith("av")) #it will return True because the string ends with "av"
d = "Gaurav"
print(d.endswith("ra")) #it will return False because the string does not end with "ra"
#startswith() function to check whether the string starts with the given substring or not   
e = "Gaurav"
print(e.startswith("Ga")) #it will return True because the string starts with "Ga"
f = "Gaurav"
print(f.startswith("ur")) #it will return False because the string does not start with "ur"