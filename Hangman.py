'''
Created on May 25, 2017

@author: davidshaw
'''
from random import randrange
from string import *

# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

secret_word = get_word()
letters_guessed = []



def word_guessed():
    answer = True
    letter_contained = [False for i in range (len(secret_word))]
    for i in range(0,len(secret_word)):
        for j in range(0,len(letters_guessed)):
            if secret_word[i] == letters_guessed[j]: 
                letter_contained[i] = True
                break
    for i in range (0,len(letter_contained)):
        if letter_contained[i] != True:
            answer = False

    return answer

def print_guessed():
    for i in range (0,len(secret_word)):
        guessed = False
        for j in range(0,len(letters_guessed)):
            if secret_word[i] == letters_guessed[j]:
                guessed = True
                break
        if guessed:
            print (secret_word[i]),
        else:
            print ('_'),

def play_hangman():
    global secret_word
    global letters_guessed
    num_guesses = 6
    while word_guessed() == False & num_guesses > 0:
        print_guessed()
        print('Guesses remaining: ' + num_guesses)
        guess = input("Next letter:")
        guessed = False
        for i in range(0,len(letters_guessed)):
            if guess == letters_guessed[i]:
                guessed = True
                break
        if guessed == False:
            letters_guessed.insert(len(letters_guessed),guess)
        else:
            num_guesses -= 1
        
get_word()
play_hangman()

