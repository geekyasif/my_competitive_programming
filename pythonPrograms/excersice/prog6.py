#------------------union of an array-------------------
# 1) Use two index variables i and j, initial values i = 0, j = 0
# 2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i.
# 3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j.
# 4) If both are same then print any of them and increment both i and j.
# 5) Print remaining elements of the larger array.

# ----------------------------------------------Union--------------------------------------------------------:
#
# Initialize union U as empty.
# Copy all elements of first array to U.
# Do following for every element x of second array:
# If x is not present in first array, then copy x to U.
# Return U.

# a1 = [1, 3, 4, 5, 7]
# b1 = [2, 3, 5, 6]

# union = a
# for i in b:
#     if i in union:
#         pass
#     else:
#         union.append(i)
# union.sort()
# print(union)
# i =0
# j =0
# while i < len(a) and j < len(b):
#     if a[i] < a[j]:
#         c.append(a[i])
#         i += 1
#     elif a[i] > a[j]:
#         c.append(a[j])
#         j += 1
#     elif a[i] == a[j]:
#         c.append(a[j])
#         i += 1
#         j += 1
#     else:
#         c.append(a[j])
#         i+=1
#         j+=1
# while i < len(a):
#     c.append(a[i])
#     i+=1
#
# while j < len(b):
#     c.append(a[j])
#     j+=1

# print(c)

# --------------------------------Intersection:---------------------------------------------
# 1) Use two index variables i and j, initial values i = 0, j = 0
# 2) If arr1[i] is smaller than arr2[j] then increment i.
# 3) If arr1[i] is greater than arr2[j] then increment j.
# 4) If both are same then print any of them and increment both i and j.
# Initialize intersection I as empty.
# Do following for every element x of first array
# If x is present in second array, then copy x to I.
# Return I.
# Time complexi
# a = {7, 1, 5, 2, 3, 6}
# b = {3, 8, 6, 20, 7}
# intersaction = []
# for i in b:
#     if i in a:
#         intersaction.append(i)
#     else:
#         pass
# intersaction.sort()
# print(intersaction)

#----------------------------for to find union --------------
a = [1,2,3,4,5]
b = [4,6,7]
c = a
for i in a:
    for j in b:
        if j not in a:
            c.append(j)
print(c)
# c= a+b
# print(set(c))

#----------------------intersection of two unsorted list-----------------
# a = [1,2,3,4,5]
# b = [4,6,7]
# c = []
# for i in a:
#     for j in b:
#         if j == i:
#             c.append(j)
# print(c)
