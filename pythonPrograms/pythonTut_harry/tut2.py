# importing os module it is use for working with files 
import os

# here we create a file in write mode
filename = "text.txt"
    # f = open(filename, 'w')
    # f.write("hello wolrd")
    # f.close()

# here we open the same file in read mode and print the value
    # f = open(filename, 'r')
    # text = f.read()
    # print(text)
    # f.close()


# here we are going to popen that is built in function in os module
# basically popen is use to access and open the file directly
file = os.popen(filename, "w")
file.write("hello popen")
file.close()
file = os.open(filename, 'r')
f = file.read()
print(f)
file.close()
