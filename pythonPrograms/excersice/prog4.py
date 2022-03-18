# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for group, users in group_dictionary.items():
# 	# Now go through the users in the group
# 		for users in group_dictionary[group]:
# 			if users in user_groups:
# 				user_groups[users].append(group)
# 			else:
# 				user_groups[users] = [group]
# 		return(user_groups)
#
# print(groups_per_user({"local": ["admin", "userA"],
# "public": ["admin", "userB"],
# "administrator": ["admin"] }))
# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups.
# Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
#---------------- program to reverse a array or list------
# Creating a List
# Creating a list
list = [1,2,3,19,5]

#printing the original list
print("Original list ",list)

# Finding the length using len() and decreasing 1 value because list starts
# from 0 and goes upto n-1
i = len(list)-1

# using while loop
print("Reversed list : -")
while i >=0:

        # we can not print i directly because it doesn't give the items of list
	print(list[i])

	i -= 1