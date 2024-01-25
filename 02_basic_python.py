print(2+4)

print(10/5)
#output here is not integer data type, but float data type

print(type(10/5))

#Main criticism about python: it is a dynamically typed language, so you don't need to specify the data type of a variable.

#Statically typed languages
a=5
print(type(a))

#Exponentiation
print(2 ** 3)

#Assigning variables 
x=5
y=x**2
print(y)

#String



a = "Hello how're you"

#Arithmetic operations on strings

#print(a*5)

#Concatenation

b = "I'm good, thank you."
print(a + "" + b)

#Indexind and slicing
#First element
print(a[0])

#Last element
print(a[-1])

#Slicing
print(a[0:5])

#How many characters does our string have?
print(len(a))

print(f'Our string has {len(a)} characters')

#Alternatively
print('Our string has {} characters'.format(len(a)))

#Have a look at logical statements

print(2==2) #True

#(2 == 3) #False (equivalent to 0)

print(True == 1)

#True evaluates to 1 and false evaluates to zero

print(True + True)

print(a == b)

#Multiple logical statements
print(2==2 and 3==3)
print(2==2 and 3==4)
#or
print(2==2 or 3==4)

#testing for inquality

print(2!=3) 

print(2<3) #true
print(2>3) #false




