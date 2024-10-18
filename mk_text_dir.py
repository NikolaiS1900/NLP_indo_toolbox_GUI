"""Function to create directories if it doesn't exist."""

import os

def handle_text_dir(dir_name: str) -> None:
    """Creates directories if it doesn't exist.
    
    Args:
        dir_name (str): Name of the directory.
    """

    current_dir = os.getcwd()

    #  List all files and directories in the current directory
    directory_contents = os.listdir(current_dir)

    find_text_dir = [item for item in directory_contents if os.path.isdir(item) and item == dir_name]

    if len(find_text_dir) == 0:
        os.mkdir(dir_name)

    else:
        pass
