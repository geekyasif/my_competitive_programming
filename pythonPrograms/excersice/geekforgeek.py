# Number of n digit numbers that do not contain 9
# print(8*pow(9,8-1))
n = 19
d = 9
new = 0
# for i in range(1,n+1):
#     if i>= d:
#         i += 1
#     else:
#         new = i
#         print(i)

# print(new)

# Find the Number which contain the digit d
# print(9%10)
N = 8
a = 0
i = 0
while N:
    a += ((10**i)*(N%9))
    N = N//9
    i+=1
print(a)
c = (10**20)*(19%9)
print(c//9)