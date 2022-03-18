word = "secret"

# list to store guess letter or _ underscore
guesses = []

# number of lives
lives = 7

# setting end of game
end_of_game = False

while not end_of_game:
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print('_',end=" ")
    print('')

    guess = input(f"Lives left {lives}, Guess the letter : ")
    guesses.append(guess)

    if guess not in word:
        lives -= 1
        if lives == 0:
            break

    end_of_game = True

    for letter in word:
        if letter not in guesses:
            end_of_game = False

if end_of_game:
    print("You found the word it was {}".format(word))
else:
    print("Game Over, The word was {}".format(word))
