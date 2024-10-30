"""This module contains the function find_word_in_text."""
import re


def find_word_in_text(word_list: list[str], text: str):
    """Find the word in the text.

    Args:
        word_list (list[str]): The list of words to search for.
        text (str): The text to search in.

    Returns:
        list[str]: The list of words that were found in the text.
    """

    lines = text.split("\n")

    findings_list_list = [re.findall(rf"\w*{word}\w*", text, re.IGNORECASE) for word in word_list]

    findings_list = set(findings_list_list[1])

    matching_lines = []

    # Loop through each line
    for line_number, line in enumerate(lines, start=1):
        # Check if any word is in the current line
        for word in findings_list:
            if word in line:
                matching_lines.append(f"{line_number}    {line}")
                break  # Exit the inner loop if a match is found and by that avoid duplicates

    return matching_lines
