# Problem Set 2, hangman.py
# Name: ShehabEldeen Ahmed  
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    tmp = [] 
    for letter in secret_word:
      tmp.append(letter in letters_guessed)

    return False not in tmp



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = list(secret_word)

    for i in range(len(secret_word)):
      if secret_word[i] not in letters_guessed:
        guessed_word[i] = '_'

    guessed_word = ' '.join(guessed_word)

    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_not_guessed = ''
    for i in string.ascii_lowercase:
      if i not in letters_guessed:
        letters_not_guessed += i

    return ' '.join(letters_not_guessed)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remaining_guesses = 6
    remaining_warnings = 3
    vowels = 'aeiou'
    won = False
    letters_guessed = []
    unique_letters = []
    check = True

    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {str(len(secret_word))} letters long.\n{'_ ' * len(secret_word)}\n")

    while remaining_guesses > 0 and won == False:
      check = True
      print(f"You have {remaining_guesses} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}.")
      
      letter = str(input("Please guess a letter: ")).lower()

      if not letter.isalpha(): #or len(letter) != 1:
        
        if remaining_warnings > 0:
          remaining_warnings -= 1
          print(f"Oops! Thst is not a valid letter. you have {remaining_warnings} warnings left: {get_guessed_word(secret_word,letters_guessed)}")
        else:
          remaining_guesses -= 1
          print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word,letters_guessed)}")
      else:
        if letter in letters_guessed:
          check = False
          if remaining_warnings > 0:
            remaining_warnings -= 1
            print(f"Oops! You've already guessed that letter. You now have {remaining_warnings} warnings left: {get_guessed_word(secret_word,letters_guessed)}")
          else:
            remaining_guesses -= 1
            print(f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {get_guessed_word(secret_word,letters_guessed)}")

        if letter not in letters_guessed:
          letters_guessed.append(letter)

        if check:
          if letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}\n{'_'*20}")
          elif letter in vowels:
            if remaining_guesses > 1:
              remaining_guesses -= 2
              print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}\n{'_'*20}")
            else:
              remaining_guesses -= 1
          else:
            remaining_guesses -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}\n{'_'*20}")

      won = is_word_guessed(secret_word, letters_guessed)

    if won:

      for letter in secret_word:
        if letter not in unique_letters:
          unique_letters.append(letter)
    
      len_unique_letters = len(unique_letters)
      total_score = remaining_guesses * len_unique_letters
      
      print(f"Congratulations, you won!\nYour total score for this game is: {total_score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was \"{secret_word}\".")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word:string, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    result = []

    if len(my_word) == len(other_word):
      # print("myword",my_word)
      # print("other_word", other_word)
      for i in range(len(my_word)):
        if my_word[i].isalpha():
          result.append(my_word[i] == other_word[i])
    #       print("resuleInside",result)
    # print("resuleOut",result)
    if False not in result and len(result) > 0:
      return True
    else:
      return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ''

    for word in wordlist:
      if match_with_gaps(my_word, word) == True:
        # print("matchWith_gaps",match_with_gaps(my_word,word))
        possible_matches += word + ' '

    # print("possibleMathced = ", possible_matches)
    if possible_matches == '':
      print("No mathces found")
    else:
      return possible_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    remaining_guesses = 6
    remaining_warnings = 3
    vowels = 'aeiou'
    won = False
    letters_guessed = []
    unique_letters = []
    check = True

    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {str(len(secret_word))} letters long.\n{'_ ' * len(secret_word)}\n")

    while remaining_guesses > 0 and won == False:
      check = True
      print(f"You have {remaining_guesses} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}.")
      
      letter = str(input("Please guess a letter: ")).lower()

      if not letter.isalpha(): #or len(letter) != 1:
        if letter == '*':
          print(f"Possible word mathces are:\n{show_possible_matches(get_guessed_word(secret_word, letters_guessed))}") 
          continue
        if remaining_warnings > 0:
          remaining_warnings -= 1
          print(f"Oops! Thst is not a valid letter. you have {remaining_warnings} warnings left: {get_guessed_word(secret_word,letters_guessed)}")
        else:
          remaining_guesses -= 1
          print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word,letters_guessed)}")
      else:
        if letter in letters_guessed:
          check = False
          if remaining_warnings > 0:
            remaining_warnings -= 1
            print(f"Oops! You've already guessed that letter. You now have {remaining_warnings} warnings left: {get_guessed_word(secret_word,letters_guessed)}")
          else:
            remaining_guesses -= 1
            print(f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {get_guessed_word(secret_word,letters_guessed)}")

        if letter not in letters_guessed:
          letters_guessed.append(letter)

        if check:
          if letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}\n{'_'*20}")
          elif letter in vowels:
            if remaining_guesses > 1:
              remaining_guesses -= 2
              print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}\n{'_'*20}")
            else:
              remaining_guesses -= 1

          else:
            remaining_guesses -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}\n{'_'*20}")

      won = is_word_guessed(secret_word, letters_guessed)

    if won:

      for letter in secret_word:
        if letter not in unique_letters:
          unique_letters.append(letter)
    
      len_unique_letters = len(unique_letters)
      total_score = remaining_guesses * len_unique_letters
      
      print(f"Congratulations, you won!\nYour total score for this game is: {total_score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was \"{secret_word}\".")
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
