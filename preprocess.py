import os
import re
import sys

def preprocess(text: str) -> str:
    """Preprocesses the text by removing all characters that are in character_to_delete.txt.
    
    Args:
        text (str): The text to preprocess.
    """

    current_dir = os.getcwd()

    #  List all files and directories in the current directory
    directory_contents = os.listdir(current_dir)

    find_preprocess_dir = [item for item in directory_contents if os.path.isdir(item) and item == "preprocess"]

    error_message = ("You need to run 'get_char_list' before running 'preprocess'.")

    if len(find_preprocess_dir) == 0:
        sys.exit(error_message)

    preprocess_dir_content = f"{current_dir}/preprocess"
    mii = os.listdir(preprocess_dir_content)

    print(mii)

    # if len(directory_contents) == 0:
    #     sys.exit(f"\n{error_message}")
    
    # if directory_contents == []:
    #     sys.exit("\nThe file 'character_to_delete.txt' is not found\n"
    #              f"{error_message}")

    # # if directory_contents[0] != "character_to_delete.txt":
    # #     sys.exit("\nThe file 'character_to_delete.txt' is not found\n"
    # #              f"{error_message}")
        
    # if directory_contents[] == "character_to_delete.txt":
    #     with open(f"{current_dir}/preprocess/character_to_delete.txt", 'r') as f:
    #         char_list_string = f.read()

    # Removes whitespace and newline characters
    # char_list_string = re.sub(r'(\s+|\n+)', '', char_list_string)

    # # Deletes all characters in character_to_delete.txt
    # translation_table = str.maketrans("", "", char_list_string)
    # preprocessed_text = text.translate(translation_table)

    # return preprocessed_text
