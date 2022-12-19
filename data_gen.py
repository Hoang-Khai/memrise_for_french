import csv
import json

# Load the JSON array of French words and the dictionary mapping French to English
with open('words.json', 'r', encoding='utf-8') as f:
    french_words = json.load(f)

with open('dictionary.json', 'r', encoding='utf-8') as f:
    french_english_dict = json.load(f)

count = 0

# Open a CSV file for writing
with open('french_english.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['French', 'English', 'Pronunciation', 'Part of speech'])
    
    # Iterate over the French words
    for word in french_words:
        # Look up the English translation in the dictionary
        try:
            english = french_english_dict[word]['english_meanings']
            pronunciation = french_english_dict[word]['phonetic']
            part_of_speech = french_english_dict[word]['pos'] if 'pos' in french_english_dict[word] else ''

            # Write a row to the CSV file
            for meaning in english.split('; '):
                writer.writerow([word, meaning, pronunciation, part_of_speech])
        except:
            count += 1
            print(f'{count}, {french_words.index(word)}')
            pass
