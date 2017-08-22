"""
Another flavor of Plagiarism detection.
This one finds the lowest common substring between two files and determines whether
or not one plagiarized the other based on the substring.
"""

import files
import common


def get_longest_common_substring(str_one, str_two):
    '''
    Returns the longest common substring between two strings.
    :param str_one: String one
    :param str_two: String two
    :return:
    '''

    print(str_one)
    print(str_two)

    list_one = str_one.split(' ')
    list_two = str_two.split(' ')

    max_len = 0
    temp_len = 0
    num_eq = 0
    ans_list = []

    '''
    for word_one in list_one:

        for word_two in list_two:
            # print(word_one, word_two)
            if word_one != word_two:
                temp_len += num_eq - 1
                ans_list.append(max_len)
                if temp_len > max_len:
                    max_len += temp_len

                num_eq = 0
                temp_len = 0
            else:
                num_eq += 1
                temp_len += len(word_one)

    temp_len += num_eq - 1
    ans_list.append(max_len)
    if temp_len > max_len:
        max_len = temp_len
        # ans_list.append(max_len)

    print(ans_list)
    print(len(str_one) + len(str_two))
    return (max_len) * 100/(len(str_one) + len(str_two))
    '''

    return 0

def lsc_driver(cur_loc):
    '''
    Driver function for the LSC algorithm.
    :param loc: Directory location.
    :return: <>
    '''

    file_list = files.get_files_in_dir(cur_loc)

    line_list = []
    for f in file_list:
        line_list.append(files.read_lines_in_file(cur_loc + '\\' + f))
        # print(line_list)

    new_line_list = []
    for line in line_list:
        new_line = list(map(common.beautify, line))
        # print(new_line)

        new_line_list.append(new_line)
        # print(new_line_list)

    lsc_matrix = []
    for i in range(len(new_line_list)):
        for j in range(len(new_line_list)):

            if i == len(lsc_matrix):
                lsc_matrix.append([])

            try:
                lsc_matrix[i].append(lsc_matrix[j][i])
            except:

                if i == j:
                    lsc_matrix[i].append(-1)
                else:
                    lsc_matrix[i].append(get_longest_common_substring(new_line_list[i][0], new_line_list[j][0]))

    return lsc_matrix