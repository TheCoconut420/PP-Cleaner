import os

def get_files_location(path):
    file_list_location = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list_location.append(os.path.join(root, file))
    return file_list_location
