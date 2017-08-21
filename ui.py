"""
User interface for the Plagiarism Checker.
"""

import os
import bag_of_words

def main():

    cur_dir = os.path.abspath(os.curdir)

    print('\n\n****************** PLAGIARISM DETECTOR ******************')

    stop = False
    while not stop:
        choice = input('Default directory is ' + cur_dir + '. Continue? ').strip()
        if choice.lower() == 'y' or choice.lower() == 'n':
            stop = True
        else:
            print('Invalid.\n')

    if choice == 'n':
        stop = False
        while not stop:
            new_dir = input('Enter new directory: ').strip()
            if os.path.isdir(new_dir):
                stop = True
                cur_dir = new_dir
            else:
                print('Invalid.\n')

    print('\n')
    bag_of_words.bag_driver(cur_dir)

main()