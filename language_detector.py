from language_detector_fingerprint_creator import get_fingerprint, read_file
import json
import sys
import glob
import os

def get_language(input_fingerprint):
    language_points_dict = {}

    fingerprints = glob.glob(os.path.join(fingerprints_directory, '*.json'))

    for fingerprint in fingerprints:
        language_dict = get_json_into_dict(fingerprint)

        result_list = []
        result_list.append(fingerprint[13:-5])

        for key in input_fingerprint:
            if key in language_dict:
                result = 1 / (input_fingerprint[key] / language_dict[key])
                result_list.append(result)
        
        average_points = 0

        for i in result_list:
            average_points += i
        
        average_points = average_points / len(result_list)

        #language_points_dict[fingerprint[13:-5]] = average_points

    language_points_dict[fingerprint[13:-5]] = average_points

    sorted_language_points_dict = dict(sorted(language_points_dict.items(), key=lambda item: item[1], reverse=True))

    return next(iter(sorted_language_points_dict))

def get_json_into_dict(file_path):
    with open(file_path, 'r') as json_file:
        output_dictionary = json.load(json_file)
    return output_dictionary

trainingdata_directory = "trainingdata/"
fingerprints_directory = "fingerprints/"

def stop_application():
    print("Stopping Application!")
    sys.exit()


file_found = False

while file_found == False:
    try:
        file_path = str(input("Please enter filename (with \".txt\" extension): "))
        if file_path == "exit":
            stop_application()
        #file_path = "example_text_de.txt"
        text = read_file(file_path)
        file_found = True
    except Exception:
        print("File not found!")

input_fingerprint = get_fingerprint(text)
#get_language(input_fingerprint)

print(get_language(input_fingerprint))
