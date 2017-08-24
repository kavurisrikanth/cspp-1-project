"""
User interface for the Plagiarism Checker.
"""

import os
import bag_of_words
import lsc
import files
import common

"""
class Matrix:
    '''    
    Matrix class.
    Added to try and print the 2D array as a matrix. But the printing is not proper. 
    '''

    def __init__(self, arr=[]):
        self._mat = arr[:]

    # def __str__(self):
    #     return list.__str__(self)

    def __str__(self):
        ans = ''
        ans += '[\n'

        ans += '(*file*)'
        for i in range(len(self._mat)):
            ans += '  ( %u )  ' % i
        ans += '\n'

        for i in range(len(self._mat)):
            ans += '(file %u)  ' %i
            for j in range(len(self._mat)):
                ans += ' (' + str(round(self._mat[i][j], 2)) + ') ' + '  '
            ans.strip()
            ans += '\n'
        ans += ']'

        return ans
"""

def main():

    # Get the present working directory
    cur_dir = os.path.abspath(os.curdir)

    # Greeting message
    print('\n\n****************** PLAGIARISM DETECTOR ******************', end='')
    print('\n ******************* SRIKANTH KAVURI *******************\n')

    # Commented out and included this functionality in proceed() in common.py
    # stop = False
    # while not stop:
    #     choice = input('Default directory is ' + cur_dir + '. Continue? ').strip()
    #     if choice.lower() == 'y' or choice.lower() == 'n':
    #         stop = True
    #     else:
    #         # Validation
    #         print('Invalid.\n')

    question = 'Default directory is ' + cur_dir + '. Continue? '
    if not common.proceed(question):
        stop = False
        while not stop:
            new_dir = input('Enter new directory: ').strip()
            # Check if the entered path is a valid path in the system.
            if os.path.isdir(new_dir):
                stop = True
                cur_dir = new_dir
            else:
                print('Invalid.\n')

    # Giving the user the option of enabling log files.
    question = '\nEnable logging? '
    if common.proceed(question):
        log_file_name = files.create_log_file(cur_dir)
    else:
        log_file_name = ''

    print('\n')

    # Call driver functions for Bag of Words and LCS
    # bag_matrix = Matrix(bag_of_words.bag_driver(cur_dir, log_file_name))
    # lsc_matrix = Matrix(lsc.lsc_driver(cur_dir, log_file_name))

    bag_matrix = (bag_of_words.bag_driver(cur_dir, log_file_name))
    lsc_matrix = (lsc.lsc_driver(cur_dir, log_file_name))

    # Print results
    print('\nBag of words matrix:')
    print(bag_matrix)
    print('\nLCS matrix:')
    print(lsc_matrix)

    # Write results to log file, if it exists.
    # If the log file doesn't exist, then the error is just ignored.
    files.write_to_file(log_file_name, '\nBag of words matrix:\n')
    files.write_to_file(log_file_name, str(bag_matrix))
    files.write_to_file(log_file_name, '\nLCS matrix:\n')
    files.write_to_file(log_file_name, str(lsc_matrix))
    files.write_to_file(log_file_name, '\n')

main()