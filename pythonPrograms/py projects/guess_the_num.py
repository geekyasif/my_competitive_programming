print("Guess the number in between 1 to 10 ")
Num = 7
numInput = int(input("Enter Number to guess :"))
for i in range(5):
    if numInput > Num:
        print("You number is greater")
        a =  5 - (i+1)
        print("chance left",a)
        numInput = int(input("Enter number again : "))
        continue
    elif numInput < Num:
        print("your number is lesser")
        a = 5 - (i + 1)
        print("chance left",a)
        numInput = int(input("Enter number again : "))
        continue
    elif Num == numInput:
        print("Congractulation you have won in ",i+1,"times")
        break
    else:
        print("you loose")
