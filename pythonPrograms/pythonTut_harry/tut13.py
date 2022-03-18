a = input("ENter number 1")
b = input("enter number 2")
try:
    print("sum is ",int(a)+int(b))
except Exception as e:
    print(e)

print("This line will run after above line will exexute or not basically ,"
      "it is use to print the errors and help to execute rest program")
