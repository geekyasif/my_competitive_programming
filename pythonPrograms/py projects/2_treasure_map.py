for i in range(3):
    for j in range(3):
        print('🪢',end=' ')
    print('\n')

user = input("Enter the row and colom to mark the treasure : ")
a = int(user[0])
b = int(user[1])

for i in range(3):
    for j in range(3):
        if i==a and j==b:
            print('❌',end=" ")
        else:
            print('🪢',end=' ')
    print('\n')