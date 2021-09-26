#rules:
# - The program must run in Python3 without error.
# - The script must ONLY stop to either ask for the next guess or because the game has been won or lost (i.e. no menus or other user input).
# - Asking the user to make her next guess must use the following text (case sensitive and a space after the colon are necessary (I think)): “Please enter your next guess: “
# - The text printed before “Please enter your next guess: “ must END in the word to be guessed with the unknown letters starred out (i.e. hello would start as ***** and change into *e*** after ‘e’ was guessed). The string must not contain any other stars.
# - The program must print either “congratulations you win” or “you lose” on exit (not case sensitive).
# - When a game is played, a word must be picked randomly (from a uniform distribution) from the word_list.txt file.
# - The word_list.txt file must be stored in the same path as your code and when you load the file don't include the path (i.e. "open('word_list.txt', ...)").
# - If the user makes 7 wrong guesses then they lose the game.
