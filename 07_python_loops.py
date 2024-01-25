#Update
#Looking at loop syntax

#for loops operate on iterables

#Let's create an iterable object
myList=[1,2,'abc']

# Let's loop through the object
for banana in myList:
    if banana == 1:
        print(banana)
    else:
        print("Item not equal to 1.")
# Loop body needs to be indented
for banana in myList:
  if banana == 1:
  print(banana)
  else:
  print("Item note equal to 1.")

#Looping over a range of values
for i in range(5): #range generates values on the fly
  print(i)

#Another way to do it
range_vals = [0,1,2,3,4,5]
for i in range_vals:
  print(i)

#Looping over a range of values with a step

