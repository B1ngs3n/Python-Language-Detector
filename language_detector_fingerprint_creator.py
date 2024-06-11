import os
import sys
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
            try:
                with open(file_path, 'r', encoding='latin1') as file:
                    return file.read()
            except Exception:
                print(f"Error while reading file: {Exception}")
                stop_application()

def write_dict_into_json(dict_input, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(dict_input, json_file, indent=4)

def get_character_frequency_dict(text_input):
    characters_to_remove = '!"`\'*/%&?#@- .,;:_\n1234567890'
    cleaned_text_input_lowercase = delete_special_characters(text_input, characters_to_remove).lower()
    character_frequency_dict = {}
    total_characters = len(cleaned_text_input_lowercase)

    for char in cleaned_text_input_lowercase:
        if char in character_frequency_dict:
            character_frequency_dict[char] += 1
        else:
            character_frequency_dict[char] = 1
    
    for key in character_frequency_dict:
        character_frequency_dict[key] = round(character_frequency_dict[key]/total_characters,5)

    sorted_dict = sort_dict_by_values_desc(character_frequency_dict)

    return sorted_dict

def delete_special_characters(text_input, characters_to_remove):
    translation_table = str.maketrans('', '', characters_to_remove)
    cleaned_text = text_input.translate(translation_table)
    return cleaned_text

def isolate_words_into_list(text_input):
    characters_to_remove = ',.:-_!§$%&/()=?*\'#+\\}][{@€$'
    text_del_special_chars = delete_special_characters(text_input, characters_to_remove)
    text_del_new_lines = text_del_special_chars.replace('\n', ' ')
    text_lowercase = text_del_new_lines.lower()
    return text_lowercase.split()

def get_word_and_word_length_frequency_dict(text_input):
    word_length_frequency_dict = {}
    word_frequency_dict = {}

    word_list = isolate_words_into_list(text_input)
    total_words = len(word_list)

    for word in word_list:
        if f"wordLength{len(word)}" in word_length_frequency_dict:
            word_length_frequency_dict[f"wordLength{len(word)}"] += 1
        else:
            word_length_frequency_dict[f"wordLength{len(word)}"] = 1

    for key in word_length_frequency_dict:
        word_length_frequency_dict[key] = round(word_length_frequency_dict[key]/total_words,5)

    sorted_word_length_frequency_dict = sort_dict_by_values_desc(word_length_frequency_dict)
    
    for word in word_list:
        if word in word_frequency_dict:
            word_frequency_dict[word] += 1
        else:
            word_frequency_dict[word] = 1

    for key in word_frequency_dict:
        word_frequency_dict[key] = round(word_frequency_dict[key]/total_words, 5)

    word_frequency_dict = dict(list(sort_dict_by_values_desc(word_frequency_dict).items())[:20])

    return {**sorted_word_length_frequency_dict, **word_frequency_dict}

def get_fingerprint(text):
    character_frequency = get_character_frequency_dict(text)
    word_length_and_ngram_frequency = get_word_and_word_length_frequency_dict(text)
    fingerprint_dict = {**character_frequency, **word_length_and_ngram_frequency}
    return fingerprint_dict

def sort_dict_by_values_desc(dict_input):
    sorted_items = sorted(dict_input.items(), key=lambda item: item[1], reverse = True)
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict

def strip_txt_from_filename(filename):
    if filename.endswith('.txt'):
        return filename[:-4]
    return filename

def stop_application():
    print("Stopping Application!")
    sys.exit()

def main():
    trainingdata_directory = "trainingdata/"
    fingerprint_directory = "fingerprints/"

    txt_files = glob.glob(os.path.join(trainingdata_directory, '*.txt'))

    for file_path in txt_files:
        text = read_file(file_path)
        fingerprint = get_fingerprint(text)
        write_dict_into_json(fingerprint, f"{fingerprint_directory}{strip_txt_from_filename(os.path.basename(file_path))}.json")

if __name__ == "__main__":
    main()