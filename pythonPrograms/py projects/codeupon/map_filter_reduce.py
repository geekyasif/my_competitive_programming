# def add(x,y):
#     return x+y
# print(add(2,3))

# ----------------------map------------------------
# def sqr(x):
#     c = x*x
#     return c
#
# a = [1,2,3,4,5]
#
# list2 = list(map(lambda x: x*x, a))
# list2 = list(map(sqr, a))
#
# print(list2)


# --------------filter-----------------------
# def is_even(x):
#     return x%2==0


b = [2,5,4,22,13,122,34,25,21]

lst = list(filter(lambda x: x%2==0, b))
# lst = list(filter(is_even, b))

print(lst)


# ---------------------------reduce--------------------
from functools import reduce
# def add(x,y):
#     return x+y

c = [1,2,3,4,5,6]
total = reduce(lambda x,y: x+y, c)
# total = reduce(add, c)
print(total)
