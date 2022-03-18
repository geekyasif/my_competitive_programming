# ----------------------------------try - except--------------------------

# try:
#     with open('test2.txt','r') as f:
#         print(f)
# except:
#     print("File not Found")
# try:
#     with open('test2.txt','r') as f:
#         print(f)
#
# except Exception as e:
#     print(e)

# with open('test2.txt','r') as f:
#     print(f)
#
# print("This is very important program")

# -----------------------------------------else and finally ----------------------------------
# try:
#     print("Hello")
# except Exception as e:
#     print(e)
# else:
#     print("This will run only when try will run")
# finally:
#     print("It will run no matter try, except, else will run or not")

# ---------------------------multiple except----------------
# try:
#     f = open('missing')
# except OSError:
#     print('It failed')
# except FileNotFoundError:
#     print('File not found')
# -------------------------raise ----------------------------
try:
    x = -1

    if x < 0:
        raise Exception("Sorry, no numbers below zero")

except Exception as e:
    print(e)



