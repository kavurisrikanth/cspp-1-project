"""
files.py

Does all file operations required for the plagiarism detector.
"""

import datetime
import os


def get_files_in_dir(loc):
    '''
    Get names of all files in a directory.
    :param loc: Directory location to read from.
    :return: List with names of all text files in loc.
    '''

    files = []
    for file in os.listdir(path=loc):
        name = file.split('.')
        if name[-1] == 'txt' and os.path.getsize(loc  + '\\' + file) > 0:
            files.append(file)

    # print(files)
    return files
# get_files_in_dir('I:\\MSIT\\IT\\projects\\testing')

def create_log_file(loc):
    '''
    Creates a log file for the project.
    :param loc: Location to create file. String.
    :return: File descriptor of the file.
    '''

    d = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # print(d)
    fd = open(loc + '\\' + '20176001_PlagF_log_' + d + '.txt', 'w')
    fd.close()

    return fd

def write_to_file(fd, text):
    '''
    Writes text to file.
    :param fd: File descriptor
    :param text: Text to write.
    :return: True if success, False if not.
    '''

    try:
        open(fd, 'a')
        fd.write(text)
        fd.close()
        return True
    except:
        return False

def read_lines_in_file(file):
    '''
    Reads lines in file, and returns them as a list.
    :param file: File name (Complete path to file)
    :return: Return list of lines in file.
    '''

    fd = open(file, 'r')
    # ans = list(fd)

    ans = []

    for line in fd:
        line.strip('., \n')
        if line != '\n':
            ans.append(line)

    fd.close()

    # print(ans)
    return ans

# create_log_file('I:\\')