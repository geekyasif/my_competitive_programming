#----------------Bubble Sorting----------------
# list = [3,2,1]
# no_of_swap = 0
# for i in range(len(list)):
#     for j in range(len(list)-1):
#         if (list[j] > list[j+1]):
#             temp = list[j]
#             list[j] = list[j+1]
#             list[j+1] = temp
#             no_of_swap += 1
#
# print(list)
#------------------------- reverse a number ------------------------------
a = 315
rev = 0

while a!=0:

    rem = a%10
    rev = rem+rev*10
    a = a//10


print(rev)