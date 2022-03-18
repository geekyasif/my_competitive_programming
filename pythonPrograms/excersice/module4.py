# def format_address(address_string):
#     # Declare variables
#     house_number = 0
#     street_name = ""
#
#     # Separate the address string into parts
#     list = address_string.split(" ")
#     # Traverse through the address parts
#     for i in list:
#     # Determine if the address part is the
#     # house number or part of the street name
#         if i.isnumeric():
#             house_number = i
#         else:
#             street_name = i
#
#     # Does anything else need to be done
#     # before returning the result?
#
#     # Return the formatted string
#     return ("house number {} on street named {}".format(house_number,street_name))
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"
#
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
# list = Drews_list[::-1]
# list2 = list + Drews_list
# a = "asif"
# a.count()
# print(list2
#
#
#
#  assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
# def combine_lists(list1, list2):
# # Generate a new list containing the elements of list2
# # Followed by the elements of list1 in reverse order
#     new_list = list2
# # Iterate till 1st element and keep on decrementing i
#     for names in reversed (range(len(list1))):
#         new_list.append(list1[names])
#     return new_list
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
# print(combine_lists(Jamies_list, Drews_list))

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence
    return guests2.update(guests1)

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
