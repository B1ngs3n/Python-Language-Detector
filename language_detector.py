from language_detector_fingerprint_creator import get_fingerprint, read_file
import json
import sys
import glob
import os

def get_language(input_fingerprint):
    language_points_dict = {}

    fingerprints = glob.glob(os.path.join(fingerprints_directory, '*.json'))

    fingerprints_dict_list = []
    fingerprints_character_frequency_dict_list = []
    fingerprints_word_length_frequence_dict_list = []

    #split that thing!

    for fingerprint in fingerprints:
        fingerprints_dict_list.append(get_json_into_dict_list(fingerprint))

    result_dict_list = []

    for key in input_fingerprint:
        result_dict = {}
        i = 0
        for fingerprint_dict in fingerprints_dict_list:
            fingerprint_name = fingerprints[i]
            if key in fingerprint_dict:
                result_dict[fingerprint_name[13:-5]] = 1 / (input_fingerprint[key] / fingerprint_dict[key])
            else:
                result_dict[fingerprint_name[13:-5]] = 0
            i += 1
        
        result_sum = 0.0
        for result in result_dict:
            result_sum += result_dict[result]
        
        for key in result_dict:
            if result_sum != 0:
                result_dict[key] = result_dict[key] / result_sum
            else:
                result_dict[key] = 0

        result_dict_list.append(result_dict)

    final_dict = {}

    for dict in result_dict_list:
        for key in dict:
            if key in final_dict:
                final_dict[key] += dict[key]
            else:
                final_dict[key] = dict[key]

    sorted_final_dict = sorted(final_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_final_dict

def get_json_into_dict_list(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    dict1 = data.get('character_frequency', {})
    dict2 = data.get('word_length_frequency', {})

    return [dict1, dict2]

def stop_application():
    print("Stopping Application!")
    sys.exit()

### MAIN ###

trainingdata_directory = "trainingdata/"
fingerprints_directory = "fingerprints/"
examples_directory = "examples/"

file_found = False

while file_found == False:
    try:
        file_path = str(input("Please enter filename: "))
        if file_path == "exit":
            stop_application()
        #file_path = "example_text_de.txt"
        text = read_file(f"{examples_directory}{file_path}.txt")
        if text == '':
            print("Input Text is empty!")
            stop_application()
        file_found = True
    except Exception:
        print("File not found!")

input_fingerprint = get_fingerprint(text)
#get_language(input_fingerprint)

#print(get_language(input_fingerprint))

result_dictionary = get_language(input_fingerprint)

for result in result_dictionary:
    print(result)

final_language_result = next(iter(result_dictionary))

print(f"Detected Language is: {final_language_result[0]}")