import glob
import json
import os
import re
import sys


def language_dictionary(language: str) -> dict:

    with open("lang_pack/sound_category_dictionary.json", "r") as json_file:
        language_dictionary = json.load(json_file)

    return language_dictionary[language]

def sound_categories(category: str, language: str) -> str:

    dictionary = language_dictionary(language)

    sound_category = dictionary[category]

    return sound_category

def inlaut(flags: list[str]) -> str:
    """For making regex searches in inlaut"""

    flags = ["mi"]

    search = "mi"

    sound_categories = "mi"

    if inlaut in flags:
        pattern = rf"\b{search}\w*"
        return pattern

    if inlaut_regex in flags:
        pattern = rf"\b{search}[{sound_categories}]\w*"
        return pattern

    if regex_inlaut in flags:
        pattern = rf"\b[{sound_categories}]{search}\w*"
        return pattern

    else:
        sys.exit()

# TODO: make flag_handler_first



# # Gemmer en generisk besked i variablen FUNK_GUIDE.
# # Denne variable kan nu bruges i funktionerne.
# FUNK_GUIDE = """
# Her kan du søge på i absolut forlyd. Du har nu følgende valg; indtaster du:

# 1     Frisøgning
# 2     Frisøgning + Lydgruppe
# 3     Lydgruppe + Frisøgning

# Ved både 2 og 3 kan du vælge at ikke indtaste noget sælg, bare vælge en lydgruppe.
# """


# # Denne funktion bruges i alle de andre funktion.
# # Den behandler og gemmer resultet fra de andre funktioner.
# # Indholdet af argumentet "resultat" og "navn" defineres i de andre funktion.
# def _make_file(result, navn):
#     set_tekst = set(result)
#     sorted_tekst = sorted(set_tekst, key=str.lower)
#     nice_list = '\n\n'.join(sorted_tekst)
#     ordliste = open(CWD+'/Result/'+navn+'_ordliste.txt', 'w', encoding='UTF8')
#     ordliste.write("" + nice_list)
#     ordliste.close()



# # Denne funktion gør det muligt at søge på lyde i forlyd
# def forlyd():
#     # Printer FUNK_GUIDE
#     print(FUNK_GUIDE)

#     # Prompter brugeren til at træffe et valg.
#     # Valget er beskrevet i FUNK_GUIDE
#     indput = input("\nIndtast dit valg: ")
#     if indput == "1":
#         indput = input("\nSkriv dit ord med eller uden regular expression: ")
#         pattern = r"\b"+indput+r"\w*"
#     elif indput == "2":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\b"+indput+Sounds()+r"\w*"
#     elif indput == "3":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\b"+Sounds()+indput+r"\w*"
#     else:
#         exit(0)

#     # søger efter mønsteret i READ_TEXT, og ignorerer forskellem mellem store og små bogstaver.
#     result = re.findall(pattern, READ_TEXT, re.IGNORECASE)

#     navn = "forlyd"
#     # Kalder funktionen _make_file(result, navn), og giver den resultat og navn.
#     _make_file(result, navn)


# def indlyd():
#     print(FUNK_GUIDE)

#     indput = input("\nIndtast dit valg: ")
#     if indput == "1":
#         indput = input("\nSkriv dit ord med eller uden regular expression: ")
#         pattern = r"\w+"+indput+r"\w+"
#     elif indput == "2":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\w+"+indput+Sounds()+r"\w+"
#     elif indput == "3":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\w+"+Sounds()+indput+r"\w+"
#     else:
#         exit(0)
#     result = re.findall(pattern, READ_TEXT, re.IGNORECASE)
#     navn = "indlyd"
#     _make_file(result, navn)


# def udlyd():
#     print(FUNK_GUIDE)

#     indput = input("\nIndtast dit valg: ")
#     if indput == "1":
#         indput = input("\nSkriv dit ord med eller uden regular expression: ")
#         pattern = r"\w*"+indput
#     elif indput == "2":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\w*"+indput+Sounds()
#     elif indput == "3":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\w*"+Sounds()+indput
#     else:
#         exit(0)

#     result = re.findall(pattern, READ_TEXT, re.IGNORECASE)
#     navn = "udlyd"
#     _make_file(result, navn)


# def hel_ord():
#     print(FUNK_GUIDE)

#     indput = input("\nIndtast dit valg: ")
#     if indput == "1":
#         indput = input("\nSkriv dit ord med eller uden regular expression: ")
#         pattern = r"\b\w*"+indput+r"\w*"
#     elif indput == "2":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\b\w*"+indput+Sounds()+r"\w*"
#     elif indput == "3":
#         indput = input("Skriv dit ord med eller uden regular expression: ")
#         pattern = r"\b\w*"+Sounds()+indput+r"\w*"
#     else:
#         exit(0)
#     result = re.findall(pattern, READ_TEXT, re.IGNORECASE)
#     navn = "hel_ord"
#     _make_file(result, navn)


# # Det er her brugeren starter når scriptet køres.

# print('''
# Tast 1 for søgning i forlyd (absolut forlyd).
# Tast 2 for søgning i indlyd.
# Tast 3 for søgning i udlyd (absolut udlyd).
# Tast 4 for søgning i det hele af ordene.

# Søgningen vil finde alle ord der opfylder dine søgekriterier, og gemme disse ord i en seperat tekstfil.
# ''')

# VALG = input("Indtast tal: ")

# if VALG == "1":
#     forlyd()
# elif VALG == "2":
#     indlyd()
# elif VALG == "3":
#     udlyd()
# elif VALG == "4":
#     hel_ord()
# else:
#     exit(0)

# print("""
# extractor.py     done running:

# word_list.txt is ready in the Result directory.

# Visit my GitHub at: https://github.com/NikolaiS1900
# I can be contacted via: sandbecks_github@protonmail.com

# Kind regards
# - Nikolai Sandbeck
# """)