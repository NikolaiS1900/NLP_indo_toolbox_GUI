"""This module contains the function do_search."""
import re


def get_value_from_json(pattern: str) -> str:
    print("")

def do_search(word_list: str, user_input_value: str, search_type_value: str) -> str:
    """Searches the word list by the user input.

    If the rune ᚱ is found, it will prompt the function to load the sound_category_dictionary.json
    and pick the value from the key between the two ᚱ.

    Args:
        word_list (str): The word list to search.
        user_input_value (str): The user input value to search for.
        search_type_value (str): The search type value to search for.

    Returns:
        str: A new word list.
    """
    #TODO make it load the json file.
    if search_type_value == "Anlaut":
        pattern = rf"\b{user_input_value}\w+"
    elif search_type_value == "Inlaut":
        pattern = rf"\w+{user_input_value}\w+"
    elif search_type_value == "Auslaut":
        pattern = rf"\w+{user_input_value}$"
    elif search_type_value == "Free Search":
        pattern = rf"\w*{user_input_value}\w*"
    else:
        pass

    result_list = re.findall(pattern, word_list, re.IGNORECASE)

    result = "\n\n".join(result_list)

    return result
