"""
files.py

Does all file operations required for the plagiarism detector.
"""

import datetime

def read_from_directory(loc):
    '''
    Read
    :param loc:
    :return:
    '''

def create_log_file(loc):
    '''
    Creates a log file for the project.
    :param loc: Location to create file. String.
    :return: File descriptor of the file.
    '''

    d = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    print(d)
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

# create_log_file('I:\\')