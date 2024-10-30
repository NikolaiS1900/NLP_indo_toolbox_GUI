from find_word_in_text import find_word_in_text

with open("text/jyske_lov.txt", "r", encoding="utf8") as file:
    text = file.read()


word_list = ["bond", "man"]

find_word_in_text(word_list, text)



