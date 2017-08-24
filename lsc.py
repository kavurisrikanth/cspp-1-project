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
    :return: (length of LCS) * 100 / (len(string one) + len(string two)), rounded to
              two digits.

    We need the longest common substring between two strings. We're doing this by
    brute force.
    The basic concept is to find the length of a subsequence based on the starting
    word of the subsequence.
    So, for each word in the first string, we search for the word in the second
    string. For every match, we store the index of the match.
    For every matched index, we increment the index and the source index and check
    for a match in the next word. And we count.

    The maximum count is the length of the Longest Common Subsequence.

    For a bit of optimization, we could store the lengths in a dictionary.
    '''

    # print(str_one)
    # print(str_two)

    list_one = str_one.split(' ')
    list_two = str_two.split(' ')

    max_len = 0
    temp_len = 0
    num_eq = 0

    # List of indices of matches (for a single word)
    match_list = []

    # Dictionary for memoization...
    lcs_dic = {}

    for ind_one in range(len(list_one)):
        match_list.clear()

        # try:
        #     max_len = lcs_dic[list_one[ind_one]]
        # except:
        for ind_two in range(len(list_two)):

            word_one = list_one[ind_one]
            word_two = list_two[ind_two]

            if word_one == word_two:
                match_list.append(ind_two)

        source_ind = ind_one
        # print(match_list)
        for ind in match_list:
            target_ind = ind
            recorded = False

            i = 1
            num_eq = 1
            temp_len = len(word_one)
            # print('\nword one: ' + word_one)
            # print('temp len init set: ' + str(temp_len))

            while (source_ind + i < len(list_one)) and (target_ind + i < len(list_two)):

                # print('temp len: ' + str(temp_len))
                # print('num eq: ' + str(num_eq))
                if list_one[source_ind + i] == list_two[target_ind + i]:
                    num_eq += 1
                    temp_len += len(list_one[source_ind + i])
                else:
                    temp_len += num_eq - 1
                    if temp_len > max_len:
                        max_len = temp_len
                        recorded = True
                        break
                i += 1

            # In case the loop exited before the match could be recorded.
            if not recorded:
                # print('temp len, not recorded: ' + str(temp_len))
                # print('num eq, not recorded: ' + str(num_eq))
                temp_len += num_eq - 1
                if temp_len > max_len:
                    max_len = temp_len

            # print('max len for ind ' + str(ind) + ' for word ' + str(list_two[target_ind]) + ': ' + str(max_len))

        lcs_dic[list_one[ind_one]] = temp_len
        # finally:
            # print('max len: ' + str(max_len) + '\n')
            # print(lcs_dic)

    '''
    BUGGY CODE.
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
    '''
    # print(max_len)
    return round((max_len) * 2 * 100/(len(str_one) + len(str_two)), 2)



def lsc_driver(cur_loc, log_file):
    '''
    Driver function for the LSC algorithm.
    :param loc: Directory location.
    :return: <>
    '''

    file_list = files.get_files_in_dir(cur_loc)

    if len(file_list) == 0:
        print('LONGEST COMMON SUBSTRING: No text files found! Exiting.')
        files.write_to_file(log_file, '\nLONGEST COMMON SUBSTRING: No text files found! Exiting.\n')
        return []

    line_list = []
    for f in file_list:
        line_list.append(files.read_lines_in_file(cur_loc + '\\' + f))
        # print(line_list)

    new_line_list = []
    for line in line_list:
        new_line = list(map(common.beautify, line))
        # print(new_line)

        new_line_list.append(new_line)
    print('\n')
    print(new_line_list)

    lsc_matrix = []
    results = []
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

                if (lsc_matrix[i][j] >= (70)) and i != j:
                    results.append((file_list[i], file_list[j], lsc_matrix[i][j]))

    print('\n\nLONGEST COMMON SUBSEQUENCE:\n')
    files.write_to_file(log_file, '\n\nLONGEST COMMON SUBSEQUENCE:\n')

    for res in results:
        files.write_to_file(log_file, '\'' + res[0] + '\' and \'' + res[1] + '\' are similar enough (' + str(res[2]) + '% similarity) to each other (to suspect plagiarism).\n')
        print('\'' + res[0] + '\' and \'' + res[1] + '\' are similar enough (' + str(res[2]) + '% similarity) to each other (to suspect plagiarism).')

    return lsc_matrix