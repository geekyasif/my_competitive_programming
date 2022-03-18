#----------- sort a list ------------
# list = [5,4,3,-2,1]
# print("Unsorted List ",list)
# # small = list[0]
# # print(small)
# for i in range(len(list)):
#     small = i
#     for j in range(i+1,len(list)):
#         if list[j] < list[small]:
#             small = j
#     if i != small:
#         temp = list[small]
#         list[small] = list[i]
#         list[i] = temp
#
# print("Sorted List ", list)


#creating a list
# list2 = [9,1,12,15,7]
#
# #printing original list
# print("Original list ",list2)
#
# # sorting list with sorted() method its take iterable argument return a list
# list3 = sorted(list2)
#
# #printing sorted list
# print("Sorted List ", list3)

# list2 = sorted(list)
# print(list2)
# list.sort()
# print(list)

# list = [4,2,9,10,1,0]
# print(list[::-1])
#
# a = 8
# b =7.3
# c = "string"
# print(type(a))
# print(type(b))
# print(type(c))

# ----------finding a number of occurance in the list ------
# taking input from user-------------
# list = []
# size = int(input("Enter the size of the list : "))
#
# for i in range(size):
#     num = int(input("Enter number : "))
#     list.append(num)
#
# n = int(input("Enter the number to find in the list : "))
# k = 0
# for i in list:
#     if i == n:
#         k += 1
#
# if k != 0:
#     print("n found",k ,"times in the list")
# else:
#     print("Not found")

# without taking input from user
# list = [1,2,2,2,3,3,4,2,1,2]
# print(list)
# n = 2
# print("Numeber to find in the list is ",n)
# k = 0
# for i in list:
#     if i == n:
#         k += 1
#
# if k != 0:
#     print("N is found ",k,'Times')
# else:
#     print("Not found")

#---------------------sorting number that only contain 0,1,2
list = [99,2,12,-2,-22,10]
# list2 = sorted(list)
# print(list2)

for i in range(len(list)):
    small = i
    for j in range(i+1,len(list)):
        if list[j] < list[small]:
            small = j

    if small != i:
        temp = list[small]
        list[small] = list[i]
        list[i] = temp

print(list)
# This sorting programm is applicable for every unsorted list
# list = [-1,-3,3,47,21,91]
# small = large = list[0]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[j] < small:
#             small = list[j]
#         if list[j] > large:
#             large = list[j]
#
# print(small)
# print(large)
# print("Range is : ",large-small)
