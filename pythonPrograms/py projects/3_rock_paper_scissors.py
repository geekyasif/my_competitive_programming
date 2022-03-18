import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock,paper,scissors]
user = int(input("0 - Rock And 1 - Paper And 2 - Scissors. Type your choice : "))
print("You choose :")
print(game_list[user])


computer_choice = random.randint(0,2)
print("Computer Choose :")
print(game_list[computer_choice])

if user == computer_choice:
    print("It's a draw. 🚩")
elif user == 0 and computer_choice == 2:
    print("You win 🎉")
elif user == 1 and computer_choice == 2:
    print("Computer Win ☠")
elif user == 2 and computer_choice == 1:
    print("You win 🎉")
elif user == 1 and computer_choice == 0:
    print("You win 🎉")
elif user == 2 and computer_choice == 0:
    print("Computer win ☠")
elif user == 0 and computer_choice == 1:
    print("Computer win ☠")
else:
    print("Wrong Input ! ☠")

