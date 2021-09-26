# rules:
# - The program must run in Python3 without error.
# - The script must ONLY stop to either ask for the next guess or because the game has been won or lost (i.e. no menus or other user input).
# - Asking the user to make her next guess must use the following text (case sensitive and a space after the colon are necessary (I think)): “Please enter your next guess: “
# - The text printed before “Please enter your next guess: “ must END in the word to be guessed with the unknown letters starred out (i.e. hello would start as ***** and change into *e*** after ‘e’ was guessed). The string must not contain any other stars.
# - The program must print either “congratulations you win” or “you lose” on exit (not case sensitive).
# - When a game is played, a word must be picked randomly (from a uniform distribution) from the word_list.txt file.
# - The word_list.txt file must be stored in the same path as your code and when you load the file don't include the path (i.e. "open('word_list.txt', ...)").
# - If the user makes 7 wrong guesses then they lose the game.

# A simple game of hangman
# Created by Chris Firth on 26 Sep 21

# import file here ###############################
# ....

# pick random rowd here ###########################
# ...

# temporary word:
word = "hello"

# assign a blank string to the hashed_word variable
hashed_word = ""

#create the hashed word by printing a * for every character of the randomly chosen word
for i in word:
    hashed_word += "*"

#print the hashed word
print(hashed_word,"\n")

# prompt user to enter a letter (this could be made into a function)
user_guess = input("Please enter your next guess: ")
# make user_guess lower case
user_guess = user_guess.lower()
# ensure the player only enters one letter at a time 
if len(user_guess) > 1:
        print("Please only enter one letter at a time")
        user_guess = input("Please enter your next guess: ")
        user_guess = user_guess.lower()

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
        print("you lose")
        break

    # prompt user to enter a letter (this could be made into a function)
    user_guess = input("Please enter your next guess: ")
    # make user_guess lower case
    user_guess = user_guess.lower()
    # ensure the player only enters one letter at a time 
    if len(user_guess) > 1:
            print("Please only enter one letter at a time")
            user_guess = input("Please enter your next guess: ")
            user_guess = user_guess.lower()