"""Preprocessing module for text preprocessing."""
import os
import re
import sys

def preprocess(text: str) -> str:
    """Preprocesses the text by removing all characters that are in character_to_delete.txt.

    Args:
        str: The text to preprocess.

    Returns:
        str: The preprocessed text.
    """

    error_message = ("You need to run 'get_char_list' before running 'preprocess'.")

    current_dir = os.getcwd()

    preprocess_dir_content = f"{current_dir}/preprocess"

    if os.listdir(preprocess_dir_content) == []:
        sys.exit("\nThe folder is empty.\n"
                 f"{error_message}")

    if len(os.listdir(preprocess_dir_content)) > 1:
        sys.exit("\nThere should be only one file in the preprocess folder\n")


    if os.listdir(preprocess_dir_content) != ["character_to_delete.txt"]:
        sys.exit("\nThe file in the preprocess folder is not 'character_to_delete.txt'\n")

    if os.listdir(preprocess_dir_content) == ["character_to_delete.txt"]:

        with open("preprocess/character_to_delete.txt", "r", encoding="utf8") as input_file:
            char_list_string = input_file.read()

        # Removes whitespace and newline characters
        char_list_string = re.sub(r'(\s+|\n+)', '', char_list_string)

        # Deletes all characters in character_to_delete.txt
        translation_table = str.maketrans("", "", char_list_string)
        preprocessed_text = text.translate(translation_table)

    return preprocessed_text
