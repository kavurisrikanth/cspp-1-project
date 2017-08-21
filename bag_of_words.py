import math
import files
from collections import Counter

class MyCounter(Counter):

    def __init__(self, dic):
        self._len = 0
        Counter.__init__(self, dic)

    @property
    def length(self):
        for ele in self.elements():
            self._len += self.__getitem__(ele)
        return self._len

def beautify(word):
    '''
    Beautifies a word. Meaning removes all alphanumerics except _ and
    converts the word to lowercase.
    :param word: A word, string.
    :return: Beautified version of word.
    '''

    NOT_ALLOWED = '~!@#$%^&*((((((+`-=[]\\{}|;\':",./<>?'
    # print(word)
    temp = word.lower()
    return temp.strip(NOT_ALLOWED)


def strip_and_split(line):
    '''
    Strips off the unnecessary chars and splits the line
    :param line: A line
    :return: List of words in line.
    '''

    if line != '\n':
        return line.strip('., \n').split(' ')

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
        if line != '\n':
           words += line.strip('., \n').split(' ')



    b_words = list(map(beautify, words))
    # temp = list(map(strip_and_split, file_lines))
    # b_words = map(beautify, temp)

    # print(words)
    # print(b_words)
    vector = MyCounter(b_words)
    return vector

def bag_driver(cur_dir):
    '''
    Driver program for bag of words.
    :param cur_dir: Current working directory. This is where the files are.
    :return: <>
    '''

    # Get all files in cur_dir as a list
    file_list = files.get_files_in_dir(cur_dir)

    # vecs will be a list of tuples.
    # This is done to make sure that we can keep track of which vector is for
    # which file.
    vecs = []

    for file in file_list:
        vector = create_vector_for_file(cur_dir + '\\' + file)
        # print(sorted(vector.elements()))

        vecs.append(vector)

    angles = []
    results = []

    for i in range(len(file_list)):
        for j in range(len(file_list)):
            # print(angles)

            if i == len(angles):
                angles.append([])
            try:
                angles[i].append(angles[j][i])
            except:

                if i == j:
                    # Comparing a file with itself makes no sense.
                    angles[i].append(-1)
                else:
                    angles[i].append(100 * (round(get_angle(vecs[i], vecs[j]), 2)))

                if (angles[i][j] >= (70/100) * vecs[i].length) and i != j:
                    results.append((file_list[i], file_list[j]))

    # for item in angles:
    #     if len(item) == 0:
    #         angles.remove(item)
    print(angles)

    for res in results:
        print(res[0] + ' and ' + res[1] + ' are similar enough to each other.')

    '''
    for vec_tup_one in vecs:
        fname_one = vec_tup_one[0]
        vec_one = vec_tup_one[1]

        for vec_tup_two in vecs:
            fname_two = vec_tup_two[0]
            vec_two = vec_tup_two[1]

            if fname_one != fname_two:
                try:
                    angles[fname_one].append((fname_two, get_angle(vec_one, vec_two)))
                except:
                    angles[fname_one]

    '''

def get_angle(vec_one, vec_two):
    '''
    Returns the angle between two vectors. Calculates the angle by computing the dot product between the two vectors
    and the lengths of the two vectors, and getting the arccos of dot_prod/(L1 * L2)
    :param vec_one: Vector one
    :param vec_two: Vector two
    :return: Angle between vectors one and two
    '''

    len_one = 0
    len_two = 0

    for ele in vec_two:
        len_two += (vec_two[ele] ** 2)
    len_two = math.sqrt(len_two)

    dot_prod = 0
    for ele in vec_one.elements():
        len_one += (vec_one[ele] ** 2)
        dot_prod += (vec_one[ele] * vec_two[ele])
    len_one = math.sqrt(len_one)

    # print(dot_prod)
    # print(len_one * len_two)

    return dot_prod/(len_one * len_two)

test_dir = 'I:\\MSIT\\IT\\projects\\testing'
bag_driver(test_dir)