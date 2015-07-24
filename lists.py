__author__ = 'cgiridhar'

#List comprehensions are more compact and faster than an explicit for loop building a list:

# def slower():
#     result = []
#     for elem in some_iterable:
#         result.append(elem)
#     return result
#
# def faster():
#     return [elem for elem in some_iterable]
#This is because calling .append() on a list causes the list object to grow (in chunks) to make space for new elements individually,
# while the list comprehension gathers all elements first before creating the list to fit the elements in one go:

L = [x**2 for x in range(9)]
print L

lists = []
lists.append(34)
print lists
lists.insert(0,30)
print lists
lists.pop()
print lists
del lists

list1 = [1,2,3]
list2 = list1
list2[1] = 33
print list2, list1