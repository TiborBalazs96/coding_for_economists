#In this file we will look at lists, dictionaries,s et, set, tuples, range, and lambda function

myList=[1, 2, 3, 4, 5]
print(myList)

print(type(myList))

#How many objects are there in our lists
print(f'There are {len(myList)} objects in our list')

#Nice thing about lists: they are flexible with respect to the objects they contain
mixedList=[1, 'two', 3.0, True]
print(mixedList)

#we can also add and remove objects from a list
mixedList.append(6)
print(mixedList)

#Removing 
mixedList.pop() #without an argument removes last item
print(mixedList)

#How many times does the integer 1 appear in my list

print(mixedList.count(1))

#reverse a list
print(mixedList.reverse())

