# faulty calculator

print("enter options :")
print(" 1 - Add")
print(" 2 - Sub")
print("enter option : ")
n = int(input())

if n == 1:
    a = int(input("Enter first number : "))
    b = int(input("Enter Second number : "))
    print("Sum is : ",(a+b)+4)
elif n == 2:
    c = int(input("Enter first number : "))
    d = int(input("Enter Second number : "))
    print("Sum is : ", (c - d) + 4)
else:
    print("Wrong input try again")