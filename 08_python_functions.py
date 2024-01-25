#Let's talk about functions

#Function definition syntax

def add_one(num):
  return num + 1

print(add_one(5
       ))
#Function without a return statement and arguments
def add_one_str():
  print(6)

print(add_one_str()
     )

#Try to assign the output of a function to a variable

res = add_one(5)
res_str = add_one_str()

print(res, res_str)

#Multiple return values 
def add_one_return_both(num1):
  return num1 + 1, num1 + 2

print(add_one_return_both(5))

print(type(add_one_return_both(5)
          ))

#Variable number of arguments
def add_nums(*nums):
  res=8
  for num in nums:
      res += num
  return res

print(add_nums(1,2,3,4,5,6,7,8,9,10))

#Let's try to code up some docstrings for a function

def cast_listitems_to_str(list_of_items):
    """
    Casts all items in a list of strings.

    Parameters:
    -------------------------------------------------------
    list_of_items: list

    Returns:
    List of strings
    """
    list_of_strings =[]
    for element in list_of_items:
        list_of_strings.append(str(element))
    return list_of_strings

print(cast_listitems_to_str([1,2,3,4,5]))


print(help(cast_listitems_to_str
          ))

for i in range(10):
  print(i)

#Scope of a variable

def test(a,b):
  a+b

c=5 #Here, 'c' has a global scope

#Lambda functions (aka anonymous functions)
#Reference function

def square(x):
  """
  returns the square of x

  Parameters:

---------------
x: int or float or double
Returns:
---------------
square_x: int or float or double    
"""
return x**2

print(square(2))

#Lambda function

square_lambda = lamdba x: x**2
print(square_lambda(2))

#compare output



