# n = 439
# y = str(bin(n))
# print(y)
# i = 0
# lst = []
# while n != 0:
#     q = n % 2
#     lst.append(q)
#     n = n // 2
#
# new = lst[::-1]
# print(new)
# j = 0
# for k in new:
#     if k == 1:
#         j += 1
#     else:
#         break
# print(j)
# print(len(max(lst)))

# cons_one = bin(n)[2:].split('0')
# print(len(max(cons_one)))

# b = {"a": 1,"b":3}
# print(b.keys())
# c = "c"
# print(len(b))
# for i in range(len(b)):
#     if  c in b.keys():
#         print("found")
#     else:
#         print("not found")
#         break

# a = "abcdo"
# f = a[0]
# l = a[-1]
#
# if((f == "a" or f=="e" or f=="i" or f=="o" or f=="u")and (f == l) ):
#     print(True)
# else:
#     print(False)
#-------------------------------------------

    # first = arr[0]
    # second = arr[0]
    # for i in arr:
    #     if i > first:
    #         second = first
    #         first = i
    #     if i > second and i < first:
    #         second = i
    # print(second)
#------------------------------------------------
# arr = [-2,-3, -6 ,-6 ,-5]
# first = second = -101
# for i in arr:
#     if i > first:
#         second = first
#         first = i
#     if i > second and i < first:
#         second = i
# print(second,first)
#-------------------------------------------------------
# convert a number into binary and find its largest consecutive 1's
# n1 = 125
# n1 = bin(n1)
# n1 = n1[2:]
# print(n1)
# # print(max(map(len,n.split('0'))))
# # n = -41
# # v = bin(n)
# # c = v[2:]
# # print(c)
# # print(len(max(c.split('0'))))
# n = 125
# i = 0
# a = ""
# while n != 0:
#     q = n % 2
#     a = a + str(q)
#     n = n // 2
#
# b = a[::-1]
# print(max(map(len,b.split('0'))))
#---------------------------Dictionary map try catch----------------------
# dict = {"asif":"12344"}
# name = "asif"
# print(f'{name}={dict[name]}')
# #---------------------------------------
# list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# l = []
# second_lowest_names = []
# scores = set()
# for i in list:
#     a = i[1]
#     scores.add(a)
# second = sorted(scores)[1]
# print(second)
# list2 = sorted(list)
# print(list2)
# for i in list2:
#     if second == i[1]:
#         print(i[0])
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append([name, score])
#     scores.add(score)
#
# second_lowest = sorted(scores)[1]
#
# for name, score in l:
#     if score == second_lowest:
#         second_lowest_names.append(name)
#
# for name in sorted(second_lowest_names):
#     print(name, end='\n')

# str = "asif"
# list = [i for i in str]
# print(list)
# list[2] = 'T'
# print(list)
# newstr = ""
# for i in list:
#     newstr += i
# print(newstr)
# s = "qA2"
#
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())
#----------------------find number of occurances of a substring in a string-----------------------------------
# a = "abcdcdc"
# b = "cdc"
# count = 0
# for i in range(len(a)):
#     if a.startswith("asif",i):
#         count += 1
#
# print(count)

# another method is using sum and startwith
# a = "abcdcdc"
# b = "cdc"
# b

#------------------------ string validation-------------------
# a = "qA2"
# print(any(i.isalnum() for i in a))
# print(any(i.isalpha() for i in a))
# print(any(i.isdigit() for i in a))
# print(any(i.islower() for i in a))
# print(any(i.isupper() for i in a))
#------------------------------------- textwrapper program------------------------
# import textwrap
# a = "abcdefghijklmnop"
# # width = 4
# wrapper = textwrap.TextWrapper(width=4)
# wordlist = wrapper.wrap(text=a)
# x = ""
# for i in wordlist:
#     x += i+'\n'
# print(x)
# c = textwrap.wrap(a,width)
# print("\n".join())

#----------------------------------------30daysofcode maxdifference-----------------------------
# a = [1,2,5]
# list = []
# for i in a:
#     for j in a:
#         list.append(i-j)
#
# print(list)
# print(max(list))
#-----------------------------fizz buzz-------------------------------
# for i in range(1,100):
#     if i%3==0:
#         print(i,"fizz")
#     if i%5 == 0:
#         print(i,"Buzz")
#     if i%3==0 and i%5==0:
#         print(i,"FizzBuzz")
#     else:
#         print(i)
# k = 0
# for i in range(3):
#     for j in range(3):
#         if (i==1 and j==0) or (i==1 and j==2):
#             print(0,end=' ')
#         else:
#             print(1,end='')
#             k = k+i
#
# print(k)

# class Calculator:
#     def power(self,n,p):
#         self.n = n
#         self.p = p
#         try:
#             if (self.n >=0 ) and (self.p >= 0):
#                return pow(n,p)
#             else:
#                 raise ValueError("n and p should be non-negative")
#         except ValueError as e:
#             return e
#
# p = Calculator()
# print(p.power(0,-10))

# n,m = map(int,input().split())
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if (j>=(n+1)-i and j<=(n+1/2)+i):
#             print('*',end=" ")
#         else:
#             print(' ',end=' ')
#     print('\n')
# print("welcome".center(11,'-'))
# for i in range(1,4):
#     for j in range(1,6):
#         if(j>=i and j<=6-i):
#             print('*',end=" ")
#         else:
#             print(' ',end=' ')
#
#     print('\n')

#------------------------------------Capitalizing the first alpha letter of any word
# for i in range(1,10,2):
#     print('-',end=" ")
# a = "hello   world  lol"
# c = a.strip()
# for i in c:
#     print(i.capitalize(),end="")

#----------------------------SCope------------

# list = [8,8,8,8,8]
# list2 = []
# for i in list:
#     for j in list:
#         if i!=j and i < j:
#             list2.append(j-i)
#         else:
#             list2.append(0)
#
# print(6/)













