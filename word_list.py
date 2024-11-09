"""Contains functions to make word lists from a text file."""

def make_word_list(text: str) -> str:
    """Makes a list of words from the text.

    This wordlist is in alpha-numeric order
    and contains no duplicates

    Args:
        text: The text to make a list of words from.

    Returns: A list of words from the text.
    """

    if not text:
        raise ValueError("Text is empty")

    if not isinstance(text, str):
        raise TypeError("Text is not a string")

    else:

        split_text = text.split()

        uniq_elems_only = set(split_text)

        sorted_list = sorted(uniq_elems_only)

        nice_list = "\n\n".join(sorted_list)

        return nice_list
