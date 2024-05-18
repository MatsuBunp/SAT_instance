import os
def find_files_without_string(directory, search_string):
    matching_files = []

    for filename in os.listdir(directory):
        with open(f"{directory}/{filename}")