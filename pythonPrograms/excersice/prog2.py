# First taking input and create a list.
size_of_array = int(input("Enter the size of an list : "))

# Creating an empty list to store n numbers
list = []
for i in range(size_of_array):
    #adding element to the list using append function
    list.append(i)

# Taking input to find the element in the list.
find_element = int(input("Enter the number to find in the list : "))

# Search the element in the list and print the result
for i in list:
    if i == find_element:
        print(True)
        break
else:
    print(False)

