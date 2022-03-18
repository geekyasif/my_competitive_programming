import random
import string

# ------------------Easy Method taking length by user--------------------
# letters = [i for i in string.ascii_letters]
# numbers = [i for i in range(10)]
# symbols = [i for i in string.punctuation]
# password = ""
# no_of_char = int(input("Enter the number of characters : "))
# no_of_nums = int(input("Enter the number of numbers : "))
# no_of_syms = int(input("Enter the number of symbols : "))

# for i in range(no_of_char):
#     password += random.choice(letters)
#
# for i in range(no_of_nums):
#     password += str(random.choice(numbers))
#
# for i in range(no_of_syms):
#     password += random.choice(symbols)
#
# print(password)



#-----------Hard Level list and shuffle taking length by user-----------

# password = []
# no_of_char = int(input("Enter the number of characters : "))
# no_of_nums = int(input("Enter the number of numbers : "))
# no_of_syms = int(input("Enter the number of symbols : "))
# for i in range(no_of_char):
#     password += random.choice(letters)
#
# for i in range(no_of_nums):
#     password += str(random.choice(numbers))
#
# for i in range(no_of_syms):
#     password += random.choice(symbols)
#
# print(password)
# random.shuffle(password)
# new_password = "".join(password)
# print(new_password)




#-----------------------Another Method  using join--------------------------------

# mix = string.ascii_letters + string.digits + string.punctuation
# print(random.choice(mix))
#
# newpassword = "".join(random.choice(mix) for i in range(random.randint(8,16)))
# print(newpassword)


# ------------Method without join-------------------
# mix = string.ascii_letters + string.digits + string.punctuation
# newnew = ""
# for i in range(random.randint(8,12)):
#     newnew += random.choice(mix)
# print(newnew)
