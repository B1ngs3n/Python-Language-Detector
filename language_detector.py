from language_detector_fingerprint_creator import get_fingerprint, read_file


def get_language(input_fingerprint):
    language_points_dict = {}



    return language_points_dict[0].key

trainingdata_directory = "trainingdata/"
file_path = "example_text_de.txt"
text = read_file(file_path)

fingerprint = get_fingerprint(text)

print(get_language(fingerprint))