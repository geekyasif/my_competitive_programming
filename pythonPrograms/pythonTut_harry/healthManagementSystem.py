import datetime
import json

def dateAndTime():
    return datetime.datetime.now()

def lock_diet():
    roti = input("Enter Number of roti : ")
    chawal = input("Enter amount of chawal in gram : ")
    daal = input("Enter amount of daaal in gram : ")
    sabji = input("Enter sabji name with amount : ")
    dateTime = f'{dateAndTime()}'
    diet_dict = {
        'dateAndTime' : dateTime,
        'roit' : roti,
        'chawal' : chawal,
        'daal' : daal,
        'sabji' : sabji,
    }
    diet_lock_file = open('diet.txt','a')
    diet_lock_file.write('\n')
    diet_lock_file.write(json.dumps(diet_dict))
    diet_lock_file.close()

def view_diet():
    view_diet = open('diet.txt','r')
    print('Your Diet')
    print(view_diet.read())
    view_diet.close()

def lock_exercise():
    ex1 = input("Enter exercise 1 name : ")
    ex2 = input("Enter exercise 2 name : ")
    ex3 = input("Enter exercise 3 name : ")
    dateTime = f'{dateAndTime()}'
    exercise_dict = {
        'dateAndTime' : dateTime,
        'ex1' : ex1,
        'ex2' : ex2,
        'ex3' : ex3,
    }
    exercise_lock_file = open('exercise.txt','a')
    exercise_lock_file.write('\n')
    exercise_lock_file.write(json.dumps(exercise_dict))
    exercise_lock_file.close()

def view_exercise():
    view_exercise = open('exercise.txt','r')
    print(view_exercise.read())
    view_exercise.close()

print('1 - Diet')
print('2 - Exercise')
ans = input("Enter number to select : ")
if ans == '1':
    print('1 - Lock Diet')
    print('2 - Retrive Diet')
    diet = input('Enter number to select : ')
    if diet == '1':
        lock_diet()
        print("Diet added successfully")
    elif diet == '2':
        view_diet()
elif ans == '2':
    print('1 - Lock Exercise')
    print('2 - Retrive Exercise')
    ex = input('Enter number to select : ')
    if ex == '1':
        lock_exercise()
        print("Exercise added successfully")
    elif ex == '2':
        view_exercise()
else:
    print('Wrong input')

