import files
from collections import Counter

def beautify(word):
    '''
    Beautifies a word. Meaning removes all alphanumerics except _ and
    converts the word to lowercase.
    :param word: A word, string.
    :return: Beautified version of word.
    '''

    NOT_ALLOWED = '~!@#$%^&*((((((+`-=[]\\{}|;\':",./<>?'

    temp = word.lower()
    return temp.strip(NOT_ALLOWED)



def create_vector_for_file(file_path):
    '''
    Creates a count vector (dictionary) for the file named file_name
    :param file_path: Full path of the file
    :return: Count dictionary of file.
    '''

    file_lines = files.read_lines_in_file(file_path)

    words = []
    for line in file_lines:
        # print('line: ' + line)
        words += line.strip('., \n').split(' ')

    b_words = list(map(beautify, words))

    # print(words)
    # print(b_words)
    vector = Counter(b_words)
    return vector

def bag_driver(cur_dir):
    '''
    Driver program for bag of words.
    :param cur_dir: Current working directory. This is where the files are.
    :return: <>
    '''

    # Get all files in cur_dir as a list
    file_list = files.get_files_in_dir(cur_dir)

    vecs = []

    for file in file_list:
        vector = create_vector_for_file(cur_dir + '\\' + file)
        # print(sorted(vector.elements()))

        vecs.append(vector)



test_dir = 'I:\\MSIT\\IT\\projects\\testing'
bag_driver(test_dir)