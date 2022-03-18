print("Welcome To My Mess System")
print("1 - Admin Login")
print("2 - Student Login")

login = input("Enter number for login : ")

if login == "1":

    print("1 - New Student Registration")
    print("2 - Get Student Details")
    ans = input("Enter Number : ")
    if ans == "1":
        name = input("Enter Student Name: ")
        branch = input("Enter Branch Name: ")
        university = input("Enter University Name: ")
        hostel = input("enter Hostel Name: ")
        mess_fees = input("Enter Advance Mess Amount: ")

        file = open(f"{name}.txt","a")
        student_id = 0
        file.write(f"Student Id : {student_id + 1}\n Name : {name} \n Branch : {branch} \n University : {university} \n Hostel : {hostel} \n Balance Fees : {mess_fees} ")
        student_id += 1
        file.close()

    elif ans == "2":
        name = input("Enter name : ")
        file =  open(f"{name}.txt",'r')
        print(file.read())
        file.close()

    else:
        print("Wrong Input!")


elif login == "2":
    name = input("Enter your Name : ")
    try:
        file = open(f"{name}.txt","r")
        print(file.read())
        file.close()
    except:
        print("Name Not Found")

else:
    print("Wrong Input!")


