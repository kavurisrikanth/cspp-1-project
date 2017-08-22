"""
User interface for the Plagiarism Checker.
"""

import os
import bag_of_words
import lsc

def main():

    cur_dir = os.path.abspath(os.curdir)

    print('\n\n****************** PLAGIARISM DETECTOR ******************', end='')
    print('\n ******************* SRIKANTH KAVURI *******************')

    stop = False
    while not stop:
        choice = input('Default directory is ' + cur_dir + '. Continue? ').strip()
        if choice.lower() == 'y' or choice.lower() == 'n':
            stop = True
        else:
            print('Invalid.\n')

    if choice.lower() == 'n':
        stop = False
        while not stop:
            new_dir = input('Enter new directory: ').strip()
            if os.path.isdir(new_dir):
                stop = True
                cur_dir = new_dir
            else:
                print('Invalid.\n')

    print('\n')
    bag_matrix = bag_of_words.bag_driver(cur_dir)

    # For Bag of words submission on 22-8-17.
    # lsc_matrix = lsc.lsc_driver(cur_dir)

    print(bag_matrix)
    # print(lsc_matrix)

main()