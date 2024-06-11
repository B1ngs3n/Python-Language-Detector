from iso639_language_codes import get_language_name_by_id
from language_detector_fingerprint_creator import get_fingerprint, read_file
import json
import sys
import glob
import os
from collections import Counter
import argparse

def get_language(input_fingerprint, fingerprints_directory):
    fingerprints = glob.glob(os.path.join(fingerprints_directory, '*.json'))

    fingerprints_dict_list = []

    for fingerprint in fingerprints:
        fingerprints_dict_list.append(get_json_into_dict(fingerprint))

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

def get_json_into_dict(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    return data

def stop_application():
    print("Stopping Application!")
    sys.exit()

def main():
    fingerprints_directory = "fingerprints/"
    examples_directory = "examples/"
    file_found = False

    if len(sys.argv) > 1:
        file_path = sys.argv[1]        
        try:
            text = read_file(f"{examples_directory}{file_path}.txt")
            if text == '':
                print("Input Text is empty!")
                stop_application()
            file_found = True
        except Exception:
            print("File not found!")

    while not file_found:
        try:
            file_path = str(input("Please enter filename (including '.txt'): "))
            if file_path == "exit":
                stop_application()
            text = read_file(file_path)
            if text == '':
                print("Input Text is empty!")
                stop_application()
            file_found = True
        except Exception:
            print("File not found!")

    input_fingerprint = get_fingerprint(text)
    result_dictionary = get_language(input_fingerprint, fingerprints_directory)

    for result in result_dictionary:
        print(result)

    final_language_result = next(iter(result_dictionary))
    detected_language_string = get_language_name_by_id(final_language_result[0])
    print(f"Detected Language is: {detected_language_string}")

if __name__ == "__main__":
    main()