import os
def read_txt_file(filename):
    
    # Get the directory of the current script
    base_dir = os.path.dirname(__file__)
    # Construct the absolute path to the text file
    file_path = os.path.join(base_dir, 'files', filename)
    with open(file_path, 'r') as file:
        strings=file.read()
        string_list =strings.split(" ")
        print(len(string_list))

read_txt_file('words1.txt')