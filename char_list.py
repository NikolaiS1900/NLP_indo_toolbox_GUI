"""Contains function that creates a list with individual characters."""

import re

def char_list(text: str) -> str:
    """Makes an overview of all individual characters in thetext."""

    #  Removes whitespace and newline characters
    text = re.sub(r'(\s+|\n)', '', text)

    #  Makes a list of all characters in the text
    character_list = set(text)

    #  Sorts the characters in alpha-numeric order.
    #  key=str.lower makes sure that the sorting is case-insensitive
    sorted_characters_list = sorted(character_list, key=str.lower)

    sorted_characters_string = " ".join(sorted_characters_list)

    return sorted_characters_string
