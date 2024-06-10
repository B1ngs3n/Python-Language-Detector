import re
import os
import glob
import json

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='utf-16') as file:
                return file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin1') as file:
                return file.read()

def write_dict_into_json(dict_input, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(dict_input, json_file, indent=4)

def get_character_frequency_dict(text_input):
    character_frequency_dict = {}
    total_characters = len(text_input)

    for char in text_input:
        if char in character_frequency_dict:
            character_frequency_dict[char] += 1
        else:
            character_frequency_dict[char] = 1
    
    for key in character_frequency_dict:
        character_frequency_dict[key] = round(character_frequency_dict[key]/total_characters,10)

    return sort_dict_by_values_desc(character_frequency_dict)

def delete_special_characters(text_input):
    deletion_pattern = r"[()\.\,,\-#@!?\n ]"
    return re.sub(deletion_pattern, "", text_input)

def get_word_length_frequency_dict(text_input):
    word_length_frequency_dict = {}
    words = re.findall(r'\b\w+\b', text_input)
    total_words = 0

    for word in words:
        total_words += 1

        if f"wordLength{len(word)}" in word_length_frequency_dict:
            word_length_frequency_dict[f"wordLength{len(word)}"] += 1
        else:
            word_length_frequency_dict[f"wordLength{len(word)}"] = 1

    for key in word_length_frequency_dict:
        word_length_frequency_dict[key] = round(word_length_frequency_dict[key]/total_words,10)

    return sort_dict_by_values_desc(word_length_frequency_dict)

def get_fingerprint(text):
    character_frequency = get_character_frequency_dict(delete_special_characters(text))
    word_length_frequency = get_word_length_frequency_dict(text)
    fingerprint_dict = {**character_frequency, **word_length_frequency}
    return fingerprint_dict

def sort_dict_by_values_desc(dict_input):
    sorted_items = sorted(dict_input.items(), key=lambda item: item[1], reverse = True)
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict

def strip_txt_from_filename(filename):
    if filename.endswith('.txt'):
        return filename[:-4]
    return filename

### MAIN ###

trainingdata_directory = "trainingdata/"
fingerprint_directory = "fingerprints/"

txt_files = glob.glob(os.path.join(trainingdata_directory, '*.txt'))

for file_path in txt_files:
    text = read_file(file_path)
    fingerprint = get_fingerprint(text)
    write_dict_into_json(fingerprint, f"{fingerprint_directory}{strip_txt_from_filename(os.path.basename(file_path))}.json")