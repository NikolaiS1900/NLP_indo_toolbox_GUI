import json

from word_list_search import do_search

with open ("word_list.txt", "r", encoding="utf8") as file:
    word_list = file.read()

user_input_value = "þæᚱnaᚱ"

search_type_value = "Free Search"

selected_language = "Danish_Norwegian_Swedish"

with open ("lang_pack/sound_category_dictionary.json", "r", encoding="utf8") as json_file:
    sound_category_dictionary = json.load(json_file)

"ᚱ"

search_result = do_search(word_list, user_input_value, search_type_value, selected_language, sound_category_dictionary)

print(search_result)
