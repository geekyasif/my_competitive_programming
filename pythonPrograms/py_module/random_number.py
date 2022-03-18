import random

# generating random number from 1 to 6 using randint method
c = random.randint(1,6)
print(c)



# printing random value from the list using choice method
list = ["head", "tail","dog", "cat"]
print(random.choice(list))

# shuffling the list using shuffle method
numbers = [2,43,1,4,243,11,109]
random.shuffle(numbers)
print(numbers)