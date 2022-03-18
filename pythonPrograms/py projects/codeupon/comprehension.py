# comprehesnion :- it is the advance features of map filter and reduce
# list comprehension :-  It is a most pythonic way to create a list or it is

# l2 = [i for i in range(10) if i%2==0]
# print(l2)

# set comprehension :- We can create a set using coprehension
# l3 = {i for i in range(10) if i%2!=0}
# print(l3)

# dictionary comprehennsion :-  We can create a dictionary using comprehsnsion
# l4 = {k:k*4 for k in range(10)}
# print(l4)

#generator comprehension : we can also create generator using
gen = (i for i in range(10))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())