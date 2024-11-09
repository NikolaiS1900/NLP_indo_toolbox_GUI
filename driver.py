import json

from word_list_search import get_value_from_json
from load_json import load_json

dictionary = load_json("lang_pack/sound_category_dictionary.json")


word_list = get_value_from_json("oᚱnaᚱᚱveᚱ", "Danish_Norwegian_Swedish", dictionary)

print(word_list)