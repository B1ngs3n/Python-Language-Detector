import difflib
import sys
import json

with open('iso639_language_codes.json', 'r', encoding='utf-8') as file:
     languages = json.load(file)

language_to_code = {}

for code, name in languages.items():
    for sub_name in name.split(', '):
        language_to_code[sub_name.strip().lower()] = code

def get_language_name_by_id(id):
    if id.upper() in languages:
        return languages[id.upper()]
    return f"{id} - Unknown Language Code"

def get_language_code_by_name(name):
    closest_match = difflib.get_close_matches(name.lower(), language_to_code.keys(), n=1, cutoff=0.6)
    if closest_match:
        return language_to_code[closest_match[0]]
    return "Unknown language name"

def main():
    _input = input("1 - Get Language Name by Language Code \n2 - Get Language Code by Language Name \n")

    if _input == "1":
        print(get_language_name_by_id(input("Enter Language Code: ")))
    elif _input == "2":
        print(get_language_code_by_name(input("Enter Language Name: ")))
    else:
        print("Invalid Input")

    sys.exit()

if __name__ == "__main__":
    main()
