# list = [1,2,3,4,5,6]
# large = list[0]
# m = len(list)
# z = m+1
# for i in range(z):
#     if i > large:
#         large = i
#
# print(large)
#
# from numpy import array
# def small(arr):
#     small = arr[0]
#     for i in arr:
#         if i> small:
#             small = i
#     return small
#
# arr = array([1,3,4,5,34])
# print(small(arr))
#
# def minimum(list):
#   current_min = list[0]  # Start by assuming the first number is smallest
#   for num in list:       # Loop through each number in the list
#     if num < current_min:
#       current_min = num  # Update current_min if current number is less
#   return current_min
#
# print (minimum([1,2,3,-1]))



# Creating a list
# list = [1,8,10,112,9,0]
# print(min(list))
# print(max(list))
# Creating two variables called small and large and assign the first element of the list
# small = large = list[0]
#
# # Now with the for loop we compare the each element of the list to the fisrt element and according to
# #     the condition we assign the value into those variables and we get the small and large value from the list.
# for i in list:
#     if i > large:
#         large = i
#     if i < small:
#         small = i
#
# print(large)
# print(small)
# print(min(list))
# print(max(list))
#Create a list
# list = [2,90,8,1,0,100]
# smallest = min(list)
# largest = max(list)
# print("Smallest ",smallest)
# print("Largest ",largest)

# Creating a list
# list1 = [12,3,123,11,6,1,0,1223]
# list1.sort()
#
# print("Smallest ",list1[0])
# print("Largest ",list1[-1])
# Creating a list
# list = [12,3,123,11,6,1]
#
# # Sorting the list in ascending order
# list.sort()
#
# # By using indexing method we get the smallest and largest element
# print("Smallest ",list[0])
# print("Largest ",list[-1])