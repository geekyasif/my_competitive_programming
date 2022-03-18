# ******** map **********
# map() is a function that apply on interable items

# def sum(a):
#     return a*a
#
# lst = [1,2,3,4,5]
# lst2 = list(map(sum,lst))
# print(lst)

#********************************
# lst = [1,2,3,4,5]
# map function takes two argument
# first a function and second a iterable items
# return an object and you can use list to store those objects
# lst2 = list(map(lambda i: i*i, lst))
# print(lst2)

#*********************************
# str = "abc"
# str2 = list(map(lambda i:i+".py",str))
# print(str2)

#*****************************
# def sqr(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [sqr,cube]
# list4 = [2,4,1,9,10]
# for i in list4:
#     list3 = list(map(lambda x:x*x,list4))
#     print(list3)
#
# #****************************
# list3 = list(map(lambda x:x*x,list4))
# print(list3)

#********************* filter *************************
# filter is same like map but it return only true value
# lets check an example

list2 = [1,2,3,4,5,6,7,8,9,10]
is_greater = list(filter(lambda x:x>5, list2))
print(is_greater)