from language_code_translator import get_language_name_by_id
from language_detector_fingerprint_creator import get_fingerprint, read_file
import json
import sys
import glob
import os

#Function to detect the language of a given text
def get_language(input_text, fingerprints_directory):
    #Generate 'fingerprint'
    input_fingerprint = get_fingerprint(input_text)
    language_fingerprints = glob.glob(os.path.join(fingerprints_directory, '*.json'))

    fingerprints_dict_list = []

    for fingerprint in language_fingerprints:
        fingerprints_dict_list.append(get_json_into_dict(fingerprint))

    result_dict_list = []

    for key in input_fingerprint:
        result_dict = {}
        i = 0
        for fingerprint_dict in fingerprints_dict_list:
            fingerprint_name = language_fingerprints[i]
            if (key not in fingerprint_dict or fingerprint_dict[key] == 0):
                result_dict[fingerprint_name[13:-5]] = 0
            else:
                result_dict[fingerprint_name[13:-5]] = 1 / (input_fingerprint[key] / fingerprint_dict[key])
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

    #Most Likely Languages is a list 
    most_likely_languages_dict = sorted(final_dict.items(), key=lambda item: item[1], reverse=True)

    #Detected Language is the name of the language that is the first item in the sorted list of possible languages
    detected_language_id = next(iter(most_likely_languages_dict))[0]
    detected_language = get_language_name_by_id(detected_language_id)
    return f"{detected_language_id} - {detected_language}"

def get_json_into_dict(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    return data

def stop_application():
    print("Stopping Application!")
    sys.exit()

def main():
    fingerprints_directory = "fingerprints/"
    file_found = False

    if len(sys.argv) > 1:
        file_path = sys.argv[1]        
        try:
            text = read_file(file_path)
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

    print(f"Detected Language is: {get_language(text, fingerprints_directory)}")

if __name__ == "__main__":
    main()