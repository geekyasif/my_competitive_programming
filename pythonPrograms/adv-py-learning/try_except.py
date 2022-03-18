try:
    f = open("doesn't_exists_file.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print("It will run no matter try or else will run or not")


