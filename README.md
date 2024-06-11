# Language Detector

## Overview

This project is designed to detect the language of a given text using fingerprinting techniques. It consists of two main components:

1. `language_detector.py`: Detects the language of an input text based on precomputed language fingerprints.
2. `language_detector_fingerprint_creator.py`: Generates fingerprints for different languages based on training text data.

## Files

- **language_detector.py**
- **language_detector_fingerprint_creator.py**

## Setup

### Prerequisites

Make sure you have Python installed on your system. Additionally, install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Dependencies

- `iso639_language_codes`
- `json`
- `argparse`
- `glob`
- `os`
- `collections`
- `sys`

## Usage

### 1. Generate Language Fingerprints (or use the ones I already created)

To generate language fingerprints, place your training text files in the `trainingdata/` directory. Each file should be named according to the language it represents (e.g., `EN.txt`, `ES.txt`).

Run the following command:

```bash
python language_detector_fingerprint_creator.py
```

This script will create JSON files in the `fingerprints/` directory, each containing the fingerprint of the corresponding language.

The fingerprints will get created using the "trainingdata" files for the languages. You can add your own text to improve the quality of the fingerprints.

### 2. Detect Language

To detect the language of an input text, use the `language_detector.py` script. You can provide the input text file and the directory containing the fingerprints as arguments.
Otherwise you will get asked for the path to a .txt file.

Run the following command:

```bash
python language_detector.py <file_path>
```

For example:

```bash
python language_detector.py sample.txt
```

### Script Details

#### language_detector.py

This script includes the following functions:

- **get_language(input_fingerprint, fingerprints_directory)**: Compares the input fingerprint with stored fingerprints to determine the most likely language.
- **get_json_into_dict(file_path)**: Loads a JSON file into a dictionary.
- **stop_application()**: Prints a stopping message and exits the application.
- **main()**: Main function to handle argument parsing and initiate language detection.

#### language_detector_fingerprint_creator.py

This script includes the following functions:

- **read_file(filename)**: Reads the content of a file.
- **write_dict_into_json(dict_input, filename)**: Writes a dictionary into a JSON file.
- **get_character_frequency_dict(text)**: Computes the character frequency distribution in the text.
- **get_word_and_word_length_frequency_dict(text)**: Computes word and word length frequency distribution in the text.
- **get_fingerprint(text)**: Generates a fingerprint for the given text.
- **sort_dict_by_values_desc(dict_input)**: Sorts a dictionary by its values in descending order.
- **strip_txt_from_filename(filename)**: Strips the `.txt` extension from a filename.
- **stop_application()**: Prints a stopping message and exits the application.
- **main()**: Main function to generate fingerprints from training data.

## Supported Languages 

Currently this script is only supporting the following languages:
- CS - Czech
- DA - Danish
- DE - German
- EN - English
- ES - Spanish
- FR - French
- IT - Italian
- JA - Japanese
- KO - Korean
- NL - Dutch
- NO - Norwegian
- PL - Polish
- PT - Portuguese
- RU - Russian
- SV - Swedish
- TR - Turkish
- VI - Vietnamese
- ZH - Chinese

### Add more languages

To detect a language, the script needs a "fingerprint" which is a json file with the name "<language_code>.json".
To generate a fingerprint, create a ".txt" file inside the "trainingdata" directory and name it "<language_code>.txt".
Trainingdata files should contain as much text as possible while using only common words in each language. 

#### Language Code

You can use "get_language_name_by_id(language_code)" from iso639_language_codes.py to get the full name of a language from the language code.
