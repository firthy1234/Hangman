# A simple game of hangman by Chris Firth
# Created on 26 Sep 21. Last updated 8 Oct 21

import random                         # import the random library
file = open("word_list.txt","r")      # open the word list file
words = file.readlines()              # read the contents of each line of the file
word = random.choice(words)           # pick a random word from the words list
word = word[:-1]                      # remove the \n from the word
hashed_word = ""                      # assign a blank string to the hashed_word variable

for character in word:                # create the hashed word by printing a * for every character
    hashed_word += "*"                # of the randomly chosen word

def message():                        # define a function to prompt the user to enter a letter
    user_guess = input("Please enter your next guess: ")
    user_guess = user_guess.lower()   # make user_guess lower case
    while len(user_guess) != 1:       # ensure the player only enters one letter at a time 
        print("Please only enter one letter at a time")
        user_guess = input("Please enter your next guess: ")
        user_guess = user_guess.lower()
    return user_guess

lives = 7                             # The lives variable will decrement with each incorrect guess

while lives:                          # while the players has lives remaining 
    correct_guess = False             # start by resetting correct_guess to false
    print("\n",hashed_word,"\n")      # print the current hashed word (includes any correct guesses)   
    user_guess = message()            # call message() and assign the return to user_guess

    for i in range(len(word)):        # check each letter in word for a match against user_guess
        # if user_guess matches a character in word, replace that character in hashed_word
        if user_guess == word[i]:
            hashed_word = hashed_word[:i] + user_guess + hashed_word[i+1:]
            correct_guess = True      # set correct_guess to True
     
    if not correct_guess:             # if correct_guess is still False: 
        lives -= 1                         # - remove a life 
        print(lives, "lives remaining...") # - inform the player of the number of lives remainig

    if hashed_word == word:           # if the player guesses all the letters: 
        print("Answer:  ",word)            # - print the word the player was trying to guess
        print("Congratulations, you win!") # - inform the player they've won
        break                              # - break the while loop
    
    if lives == 0:                    # if lives gets to zero:
        print("Answer:  ",word)            # - print the word the player was trying to guess
        print("Sorry, you lose.")          # - inform the player they've lost
        break                              # - break the while loop