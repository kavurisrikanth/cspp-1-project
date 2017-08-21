import files

def create_vector_for_file(file_path):
    '''
    Creates a count vector (dictionary) for the file named file_name
    :param file_path: Full path of the file
    :return: Count dictionary of file.
    '''

    file_lines = files.read_lines_in_file()

def bag_driver(cur_dir):
    '''
    Driver program for bag of words.
    :param cur_dir: Current working directory. This is where the files are.
    :return: <>
    '''

    file_list = files.get_files_in_dir(cur_dir)

