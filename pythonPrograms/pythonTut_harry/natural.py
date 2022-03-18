# a = 'sgring'
# b = ''
# print(repr(a or b))
#
# c = int(5)
# print('%d'%(c))
#
# line = "Hello \nMohmmad \nAsif"
# print(line.split())
# print(line.split(' ',1))
#
# def hello():
#     '''This is a helllo Function'''
#     print("Hello Function")
#
# print(hello.__doc__)

# a = "malayalam"
# if a == a[::-1]:
#     print("Palindrome string")
# else:
#     print("not palindrome")
#

# list1=[]
# list2=[]
# for i  in range(1,21):
#     list1.append(4*i-3)
#
# for i in range(0,20):
#     list1.append(list1[i]%2==1)
#
# print(all(list2))
#
#
# list3 = []
# list4 = []
#
# for i in range(1,21):
#     list3.append(4*i)
#
# for i in range(0,20):
#     list4.append(list3[i]%200==0)
#
# print(any(list4))
#
# print("Welcome", "to","webdecode","Mohammad" ,"Asif",sep='-')
# print("webdevcode" , end = ' ')
# print("Is the channel to learn programming in the collage")
#
# print("Hello" ,"%2d" %(9111))
# a = '{}'.format('bro')
# print(a,"Hello {} {}" .format('geek','asif'))

# a = 'stringabcasifdef'
# b= 'abc'
# print(a.find(b))
#
# c = []
# d = []
# if c is d:
#     print('true')
# else:
#     print('false')

# file2 = open('text.txt','r')
# print(file2.read())

# print(' 1 - for Diet')
# print(' 2 - for Exercise')
# a = int(input('Enter a  number: '))
# if a == 1:
#     file = open('diet.txt','a')
#     diet1 = input("Enter number of roti : \n",)
#     file.write(diet1)
#     file.close()
# elif a == 2:
#     print('Exercise')

# str = "arcade"
# print(str.count('e'))
# from datetime import datetime
# #
# def dateandtime():
#     return datetime.now()
#
# print('[',dateandtime(),']',' 2 roti and 1 chawal full plate')

# ************************ insert dictionary into file using json.dumb ***********************
import json
# file = open('text.txt','a')
# dict = {
#     'name' : 'asasaif',
#     'diet': 'Fat buring',
#     'exercise' : 'chest press'
# }
# for diet_name , diet_value in dict.items():
#     print(diet_name + ':' + diet_value)
# file.write('\n')
# file.write(json.dumps(dict))

# file2 = open('text.txt','r')
# file2.close()

# *************************** date time ***************************************
# import datetime
# def dateandtime():
#     return datetime.datetime.now()
# print(dateandtime())

# ********************************** apennding list ***************************
# list1 = [1,'harry',3,'asif']
# list1.append(5)
# print(list1)
# list1.insert(3,'Mohammad')
# print(list

# ************************  random number generator**********************
# import random
# num = random.randint(0,10)
# print(num)


# ********************** prime number *******************************
# a = int(input('Enter a number : '))
# if  a==1:
#     print("Not Prime number")
# elif a==2:
#     print('Prime Number')
# else:
#     i = 2
#     while (i<10):
#         if a%i == 0:
#             print('not prime')
#             break
#         elif a%i !=0:
#             if i == a-1:
#                 print('prime number')
#                 break
#             else:
#                 i = i + 1

# **************************** factorial ********************************
# list = []
# i =2
# while(i<=a):
#     if a%i == 0:
#         list.append(i)
#         i = i+1
#     else:
#         i = i +1
# print(list)


# a = "asif";
# b=''
# for i in a:
#    b  = i + b
# print(b)


# ******* prime number ********
# num = 127
# for i in range(2,num):
#    if num % i == 0:
#       print("not prime")
#       break
# else:
#    print("prime")


# import array as arr
#
# a = arr.array('i',[1,2,3,4,5,8,9])
# a.reverse()
# for i in a:
#    print(i,end=',')

# for i in range(1,4):
#    for j in range(1,6):
#       if (j>=i) and (j<=6-i):
#          print('*',end=' ')
#       else:
#          print(' ',end=' ')
#    print('\n')


# for i in range(1,4):
#    for j in range(1,6):
#       if (j>=4-i) and (j<=2+i):
#          print('*',end=' ')
#       else:
#          print(' ',end=' ')
#    print('\n')

# for i in range(1,4):
#    for j in range(1,6):
#       if (j>=4-i) or (j<=2+i):
#          print('*',end=' ')
#       else:
#          print(' ',end=' ')
#    print('\n')

# from array import *
# print("old array")
# arr = array('i',[1,2,3,4,5])
# # arr.insert(3,10)
# print(len(arr))
# arr.append(123)
# for i in arr:
#    print(i)
#
# newArr = array(arr.typecode,[])
# size = int(input("Enter the size of array : "))
# for i in range(0,size):
#    val = int(input("Enter value : "))
#    newArr.append(val)
#
# print(newArr)
#

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")
#
#
# def month_days(month, days):
#    print(month + " has " + str(days) + " " + "days.")
#
#
# month_days("June", 30)
# month_days("July", 30)



number = 10
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)


  # If a filesystem has a block size of 4096 bytes,
  # this means that a file comprised of only one byte will still use 4096 bytes of storage.
  # A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
  # Knowing this, can you fill in the gaps in the calculate_storage function below,
  # which calculates the total number of bytes needed to store a file of a given size?

  def calculate_storage(filesize):
     block_size = 4096
     # Use floor division to calculate how many blocks are fully occupied
     full_blocks = filesize // block_size
     # Use the modulo operator to check whether there's any remainder
     partial_block_remainder = filesize % block_size
     # Depending on whether there's a remainder or not, return
     # the total number of bytes required to allocate enough blocks
     # to store your data.
     if partial_block_remainder > 0:
        return full_blocks * (full_blocks + 1)
     return full_blocks * 4096



print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192




