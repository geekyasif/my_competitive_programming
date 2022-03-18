# file handling in python :- Working with files with the help in python is called file handling
# basically file handling is creating a file to store data or reading a file for data with the help of python is
#     called file handing
# There are two ways to handle with file called read and write
#
# lets talk about how to write file :
# there are few mode to open the file
# 'r' - read mode  You can only read a file it is by default
# 'w' - write mode you can write a file if it present all the data is rewrite if the file is not present it will created
# 'a' - append mode :- Means you can write a file without erasing the previous data add more to the file
# 'x'  exclasive creation :-  if a file is already exists then it will fail if the
# file is not exists it will  create a file
#'t' text mode :- opening the text file it is by default
# 'b' :- binary mode :- open the binary file
# '+' :- read and write mode :- it is used to update the file

# open() function :- this function is used to read and write the file. it takes
# two argument first is filename and second is mode in which mode you want to
# open the file

# close() function :- this function is used to close the opening file it is
# used when all the work with file is done

# read() function  : - Reading content from a file it its a argument where
# you can also give the number char to access it is not optional


# lets see an example to
f = open('test.txt')
content = f.read()
print(content)
f.close()

# readline() function :- this is used to read only one line from the file
# redlines() function :- it is used to store all the content into a list

# f = open("test.txt",'r')
# print(f.readlines())

#--------------------------------- writing a file ------------------
# write() function :- this function is used to write text into the file
# f = open('test.txt','w')
# f.write("adding new line")
# f.close()


# -------------------------appending a file ----------------------
# f = open('test.txt','a')
# f.write("\nAppednig  a new line into the file \n")
# f.close()


# -----------------------------hadnling the file in both reading and writing mode at same time-----------------
# f = open('test.txt', 'r+')
# print(f.read())
# f.write("\nadding more")
# f.close()

#-------------opening the file using with open method----------------------
# with open('test.txt','r') as f:
#     print(f.read())


