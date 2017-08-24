"""
Use the fingerprinting method to compare two files.
"""

import files
import common
from bag_of_words import create_vector_for_file
from collections import Counter

def make_k_grams(line, k):
    '''
    Generates k grams for a line. Assumes that the line has no spaces and no unallowed characters.
    :param line: A line.
    :return: A list of k-grams of line.
    '''

    # print(line)
    ans = []
    i = 0
    while i < len(line) - (k - 1):
        ans.append(line[i:i+k])
        i += 1

    return ans

def generate_p(line_one, line_two):
    '''
    Generates a value for p to use in 0 mod p.
    This value is for two files.
    :param line_one: Line in File one
    :param line_two: Line in File two
    :return: p, int
    '''

    # lines_one = files.read_lines_in_file(file_one)
    # lines_two = files.read_lines_in_file(file_two)
    #
    # if len(lines_one) > 0 and len(lines_two) > 0:
    #     line_one = common.beautify(lines_one[0])
    #     line_two = common.beautify(lines_two[0])

    # print(line_one,line_two)

    lens = list(map(len, (line_one + ' ' + line_two).split()))
    # print(lens)

    len_vec = Counter(lens)
    # print(len_vec)
    p = len_vec.most_common(1)[0][0]

    return p

def generate_fingerprints(line, k, p):
    '''
    Generate the fingerprint for a file.
    This function generates k-grams, passes them through a Hash function, and picks fingerprints from the hashes.
    :param line: Line in file
    :param k: k value to generate k-grams.
    :param p: To return every fingerprint that is 0 mod p
    :return: Fingerprints of file
    '''

    # line_list = files.read_lines_in_file(file)
    #
    # if len(line_list) > 0:
    #     line = line_list[0]

    # Removing the spaces from line.
    # Method 1
    # new_line = line.replace(' ', '')

    # Method 2
    new_line = ''
    stops = get_stop_words()
    for word in line.split(' '):
        # print(word)
        if word not in stops:
            new_line += word

    # print(line)
    print(new_line)

    k_grams = make_k_grams(new_line, k)

    # print(k_grams)

    fps = []
    hashes = []

    for ind in range(len(k_grams)):
        hash = generate_hash(k_grams[ind], k)
        hashes.append(hash)
        if hash % p == 0:
            fps.append(hash)

    print('k = ' + str(k))
    print(hashes)
    print(len(hashes))
    return (hashes, fps)

def generate_hash(word, base):
    '''
    Generate a hash by running word through a Hash function.
    :param word: a word, string
    :return: hash, int
    '''

    ans = 0
    # base = 10
    exp = len(word) - 1
    prime = 991

    for char in word:
        ans += (base ** exp) * ord(char)
        exp -= 1

    return ans % prime

def generate_k(line):
    '''
    Generates the k value for a file.
    :param line: Line in the file. Added as an arg to avoid recomputing.
    :return: k
    '''

    # line_list = files.read_lines_in_file(file)
    #
    # if len(line_list) > 0:
    #     line = common.beautify(line_list[0])
        # print(line)
    words = list(map(len, line.split(' ')))

    # Method 1
    # return max(words)

    # Method 2
    return (max(words) + min(words))//2


def fingerprint_two_files(file_one, file_two):
    '''
    Driver program for Fingerprinting.
    :param cur_loc: Current working location of the program.
    :return:
    '''

    cur_loc = 'I:\\MSIT\\IT\\projects\\testing\\'
    file_one = cur_loc + 'test_one.txt'
    file_two = cur_loc + 'test_two.txt'

    if file_one == file_two:
        return -1

    # p = 4

    lines_one = files.read_lines_in_file(file_one)
    lines_two = files.read_lines_in_file(file_two)

    len_one = len(lines_one[0])
    len_two = len(lines_two[0])

    if len_one > 0 and len_two > 0:

        line_one = common.beautify(lines_one[0])
        line_two = common.beautify(lines_two[0])

        # print(line_one, line_two)

        # k_one = generate_k(line_one)
        # k_two = generate_k(line_two)

        k = 10
        k_one = k
        k_two = k

        # Method 1
        # p = generate_p(line_one, line_two)

        # Method 2
        p = 1

        # k_one = 4
        # k_two = 4

        # print(line_one)
        # print(line_two)

        tup_one = generate_fingerprints(line_one, k_one, p)
        tup_two = generate_fingerprints(line_two, k_two, p)

        fp_one = tup_one[1]
        fp_two = tup_two[1]
        hash_one = tup_one[0]
        hash_two = tup_two[0]

        print(fp_one)
        print(fp_two)

        matches = 0
        for fp in fp_one:
            if fp in fp_two:
                matches += 1

        print('matches: ' + str(matches))

        percent_match_fp = matches * 2 * 100 / (len(fp_one) + len(fp_two))
        percent_match_hash = matches * 2 * 100 / (len(hash_one) + len(hash_two))

        print("hash: " + str(percent_match_hash) + " fp: " + str(percent_match_fp))

        return round(percent_match_hash, 2)

    return -1

    # print(generate_p(my_dir + 'test_one.txt', my_dir + 'test_two.txt'))

def get_stop_words():
    import os
    pwd = os.path.abspath(os.curdir)

    stops = []
    file = open(pwd + '\stop_words', 'r')

    for line in file:
        stops.append(line.strip())

    return stops

"""
def fingerprint_driver(cur_loc, log_file):
    '''
    Driver program for Fingerprinting.
    :param cur_loc: Current working location of the program.
    :return:
    '''

    file_list = files.get_files_in_dir(cur_loc)

    if len(file_list) == 0:
        print('FINGERPRINTING: No text files found! Exiting.')
        files.write_to_file(log_file, '\nFINGERPRINTING: No text files found! Exiting.\n')
        return []

    fp_results = []
    for ind_one in range(len(file_list)):
        for ind_two in range(len(file_list)):

"""
# get_stop_words()

my_dir = 'I:\\MSIT\\IT\\projects\\testing\\'
# print(fingerprint_driver(my_dir))
print(fingerprint_two_files('', ''))