"""
Contains functions used by all modules of the Plagiarism checker.
"""

import re

def beautify(word):
    '''
    Beautifies a word. Meaning removes all alphanumerics except _ and
    converts the word to lowercase.
    :param word: A word, string.
    :return: Beautified version of word.
    '''

    # NOT_ALLOWED = '~!@#$%^&*((((((+`-=[]\\{}|;\':",./<>?'
    # # print(word)
    # temp = word.lower()
    # return temp.strip(NOT_ALLOWED)

    return re.sub('[^a-z0-9_ ]+', '', word.lower())

def proceed(text):
    '''
    Gets an input from user.
    Validates user's choice and returns properly if the choice is yes or no (case insensitive)
    :param text:
    :return:
    '''

    stop = False
    while not stop:
        choice = input(text).strip()
        if choice.lower() == 'y' or choice.lower() == 'n':
            stop = True
        else:
            # Validation
            print('Invalid.\n')

    return choice.lower() == 'y'