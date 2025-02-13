import random

word_list = ["aardvark", "baboon", "camel"]

choice_word = random.choice(word_list)
guess = input("Guess the letter?\n").lower()

for letter in choice_word :
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
