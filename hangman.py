# A simple game of hangman
# Created by Chris Firth on 26 Sep 21
# Last updated 28 Sep 21

#import the random library
import random

# open the word list and send the contents to a list called words
file = open("word_list.txt","r")
words = file.readlines()

# pick a random word from the words list
#random_number = int(random.uniform(0.0, 99.0)) THIS WAS MY OLD METHOD
#word = (words[random_number]) THIS WAS MY OLD METHOD
word = random.choice(words) # This is my new method

# remove the \n from the word
word = word[:-1]

# assign a blank string to the hashed_word variable
hashed_word = ""

#create the hashed word by printing a * for every character of the randomly chosen word
for i in word:
    hashed_word += "*"

#print the hashed word
print(hashed_word,"\n")

# define a function to prompt the user to enter a letter
def message():
    user_guess = input("Please enter your next guess: ")
    # make user_guess lower case
    user_guess = user_guess.lower()
    # ensure the player only enters one letter at a time 
    while len(user_guess) != 1:
        print("Please only enter one letter at a time")
        user_guess = input("Please enter your next guess: ")
        user_guess = user_guess.lower()
    return user_guess

# call the message function and assign the return value to the user_guess variable
user_guess = message()

# this for loop runs 7 times
for x in range(7):
    
    # check each letter in word for a match against user_guess
    for i in range(len(word)):
        # if user_guess matches a character in word, replace that character in hashed_word
        if user_guess == word[i]:
            hashed_word = hashed_word[:i] + user_guess + hashed_word[i+1:]
    
    # print the current hashed word whih will include any correct guesses 
    print("\n",hashed_word,"\n")
        
    # if the user guesses all letters, the for loop breaks
    if hashed_word == word:
        print("congratulations you win")
        break
    
    #if the user fails to guess all the letters after their 7th attempt
    if x == 6:
        print(word)
        print("you lose")
        break
    
    # call the message function and assign the return value to the user_guess variable
    user_guess = message()