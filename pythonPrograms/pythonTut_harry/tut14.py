# file handing in python

"""
"r" - read the file
"w" - write the file
"x" - create a file if it is not exist
"a" - append it means add the text in the last in existing file
"t" - open the file in text mode
"b" - binary mode
"+" - open file with read and write
"""
# if ((10 >= 5*2) and (10 <= 5*2)):
#     print(True)
# else:
#     print(False)

# Duplicate list

# list = [1,2,2,4,4,5,5]
# i =0
# j=1
# for i in list:
#     for j in list:
#         if i == j:
#             list.remove(j)
#             j += 1
#         else:
#             j += 1
#
# print(list)

# # reverse an array
# from array import array
# arr = array('i',[1,2,3,4,5])
# print("Before",arr)
# arr[3]= 44
# print("After",arr)

# dict = {"name" : "asif", "class" : "bca"}
# for i in dict:
#     print(i)

# li = [3,10,99,23,100,1]
# for i in range(0, len(li)):
#     small = li[i]
#     for j in range(li[i]+1, len(li)):
#         if li[j] < small:
#             small = li[j]
d = 2100
a = d%4
print(a)
b = d%100
print(b)
c = d%400
print(c)


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 400 == 0):
        return True
    else:
        return False

    return leap


year = 2100

print( is_leap(year))

