"""Preprocessing module for text preprocessing."""
import os
import re
import sys

def preprocess(text: str, char_list: str) -> str:
    """Preprocesses the text by removing all characters that are in character_to_delete.txt.

    Args:
        text: str: The text to preprocess.
        char_list: str: The list of characters to remove from the text.

    Returns:
        str: The preprocessed text.
    """

    # Makes sure there is a folder called preprocesss
    # if it doesn't exist, it will be created
    if not os.path.exists("preprocess"):
        os.makedirs("preprocess")
    else:
        pass

    if not text and not char_list:
        raise ValueError("Text and character list are empty")

    if not isinstance(text, str):
        raise TypeError("Text is not a string")

    if not isinstance(char_list, str):
        raise TypeError("Character list is not a string")
    
    else:

        # Removes whitespace and newline characters
        char_list_string = re.sub(r'(\s+|\n+)', '', char_list)

        # Deletes all characters in character_to_delete.txt
        translation_table = str.maketrans("", "", char_list_string)
        preprocessed_text = text.translate(translation_table)

        return preprocessed_text
