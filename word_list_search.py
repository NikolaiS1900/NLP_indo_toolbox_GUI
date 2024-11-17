"""This module contains the function do_search and its sub routines."""
import re

def get_value_from_json(user_input_value: str,
                        selected_language: str,
                        sound_category_dictionary: dict
                        ) -> str:
    """Letters between ᚱs, are replaced with the value from the dictionary.

    Args:
        user_input_value (str): The user input value to search for.
        selected_language (str): The selected language.
        sound_category_dictionary (dict): The dictionary with the sound category values.

    Returns:
        str: The new user input value.
    """

    sound_dict_with_chosen_language = sound_category_dictionary[selected_language]

    search_string_list = []
    i = 0
    while i < len(user_input_value):
        # Check if any character "i" is "ᚱ"
        if user_input_value[i] == "ᚱ":
            # Find the next "ᚱ", by looking from the index after the current "ᚱ"
            end = user_input_value.find("ᚱ", i + 1)
            if end == -1:
                # No closing "ᚱ" found, just add the rest of the string
                search_string_list.append(user_input_value[i:])
                break

            # Extract the substring between the 'ᚱ's
            between_runes = user_input_value[i + 1:end]

            # Look up in the dictionary and replace if found, otherwise keep the original
            replacement = sound_dict_with_chosen_language.get(between_runes, between_runes)

            # Add the replacement to the search_string_list
            search_string_list.append(f"[{replacement}]")

            # Move the index past the closing "ᚱ"
            i = end + 1
        else:
            # Add the current character to the search_string_list if it's not "ᚱ"
            search_string_list.append(user_input_value[i])
            i += 1

    # Join all parts of the search_string_list to form the final string
    return "".join(search_string_list)


def do_search(word_list: str,
              user_input_value: str,
              search_type_value: str,
              selected_language: str,
              sound_category_dictionary: dict
              ) -> str:
    """Searches the word list by the user input.

    If the rune ᚱ is found, it will prompt the function to load the sound_category_dictionary.json
    and pick the value from the key between the two ᚱ.

    Args:
        word_list (str): The word list to search.
        user_input_value (str): The user input value to search for.
        search_type_value (str): The search type value to search for.
        selected_language (str): The selected language.

    Returns:
        str: A new word list.
    """

    if search_type_value == "Anlaut":
        pattern = get_value_from_json(user_input_value,
                                      selected_language,
                                      sound_category_dictionary
                                      )
        pattern = rf"\b{pattern}\w+"
    elif search_type_value == "Inlaut":
        pattern = get_value_from_json(user_input_value,
                                      selected_language,
                                      sound_category_dictionary
                                      )
        pattern = rf"\w+{pattern}\w+"
    elif search_type_value == "Auslaut":
        pattern = get_value_from_json(user_input_value,
                                      selected_language,
                                      sound_category_dictionary)
        pattern = rf"\w+{pattern}$"
    elif search_type_value == "Free Search":
        pattern = get_value_from_json(user_input_value,
                                      selected_language,
                                      sound_category_dictionary)
        pattern = rf"\w*{pattern}\w*"
    else:
        pass

    result_list = re.findall(pattern, word_list, re.IGNORECASE)

    result = "\n\n".join(result_list)

    return result
