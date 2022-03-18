import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
list_of_words = ['apple','dog','vegetable']

random_word = random.choice(list_of_words)
# print(random_word)
# print(6.1_hangmang_art.logo)
display = ['-' for i in range(len(random_word))]
print(display)

lives = 0

end_of_game = False

while not end_of_game:

    guess = input("Enter the letter to guess the word : ")
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        lives += 1
        if lives == 6:
            end_of_game = True
            print("You loose")
    print(stage[lives])


    print(display)



    if '-' not in display:
        end_of_game = True
        print("You win")

