import json

# Set up an empty dictionary to hold the data
data = {}

# Open the file and read through it line by line
with open("new_file.txt", "r", encoding='utf-8') as f:
    for line in f:
        # Split the line into its components
        parts = line.strip().split("/")
        french = parts[0].strip()
        phonetic = parts[1].strip()
        rest = parts[2].strip()

        # Split the rest of the line into its components
        rest_parts = rest.split(">")
        if ">" in rest:
            pos = rest_parts[0].strip()
            english = rest_parts[1].strip()
        else:
            pos = None
            english = rest_parts[0].strip()

        # Split the English meanings into a list
        english_meanings = english.split("__")
        # english_meanings = "; ".join([meaning.strip() for meaning in english_meanings if len(meaning) > 0])

        # Add the data to the dictionary
        data[french] = {
            "phonetic": phonetic,
            "english_meanings": "; ".join([meaning.strip() for meaning in english_meanings if len(meaning) > 0]),
        }
        if pos is not None:
            data[french]['pos'] = pos[1:]

# Write the dictionary to a JSON file
with open("output.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)