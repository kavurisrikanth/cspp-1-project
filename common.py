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