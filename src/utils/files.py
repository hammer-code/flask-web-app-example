import os

path = os.path.abspath('./files')

def get_list_of_files():
    for root, directors, files in os.walk(path, topdown = False):
        file_list = []
        for file in files:
            if '.txt' in file:
                file_list.append(os.path.join(root, file))

    return file_list


def create_new_file(filename, content):
    filepath = path + '/' + filename + '.txt'

    if os.path.isfile(filepath):
        return ''

    with open(filepath, 'w+') as file:
        file.write(content)

    return filepath
