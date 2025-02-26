import re
from symspellpy import SymSpell
from rapidfuzz import process

# Load SymSpell for spell correction
sym_spell = SymSpell(max_dictionary_edit_distance=2)
sym_spell.load_dictionary("./data/medical_dictionary.txt", term_index=0, count_index=1)

# Load medicine names
def load_medicine_list(filepath="./data/medical_dictionary.txt"):
    with open(filepath, "r") as f:
        medicines = [line.strip().lower() for line in f.readlines()]
    return medicines

medicines_list = load_medicine_list()

def spell_correct(text):
    """Corrects spelling errors using SymSpell."""
    corrected = sym_spell.lookup_compound(text, max_edit_distance=2)
    return corrected[0].term if corrected else text

# def extract_potential_medicines(text):
#     words = text.split()
#     matched_medicines = []

#     for i in range(len(words)):
#         match = fuzzy_match(words[i])
#         if match:
#             # Check if next word is a strength value (e.g., "500mg")
#             if i < len(words) - 1 and re.match(r"\d+mg", words[i + 1]):
#                 match += " " + words[i + 1]  # Append strength value
#             matched_medicines.append(match)

#     return list(set(matched_medicines))

def extract_potential_medicines(text):
    words = text.split()
    matched_medicines = []

    for i in range(len(words)):
        match = fuzzy_match(words[i], medicines_list)  # Pass medicines_list
        if match:
            if i < len(words) - 1 and re.match(r"\d+mg", words[i + 1]):
                match += " " + words[i + 1]
            matched_medicines.append(match)

    return list(set(matched_medicines))


import re
medicines_list = []
with open("data/medical_dictionary.txt", "r", encoding="utf-8") as file:
    for line in file:
        medicine_name = line.strip().split("\t")[0]  # Keep only the name (ignore metadata)
        medicines_list.append(medicine_name)
 
def fuzzy_match(word):
    """Matches a single word to known medicine names using fuzzy matching."""
    word = word.strip().lower()  # Ensure input is clean

    for medicine in medicines_list:
        base_name = re.sub(r"\s*\(.*?\)", "", medicine)  # Remove anything in parentheses

        if word == base_name.lower():
            return medicine  # Return the cleaned medicine name

    match = process.extractOne(word, medicines_list, score_cutoff=85)  # Increase threshold
    return match[0] if match else None

def fuzzy_match(word, medicines_list):
    """Matches a single word to known medicine names using fuzzy matching."""
    word = word.strip().lower()

    for medicine in medicines_list:
        base_name = re.sub(r"\s*\(.*?\)", "", medicine)  # Remove anything in parentheses

        if word == base_name.lower():
            return medicine

    match = process.extractOne(word, medicines_list, score_cutoff=70)
    return match[0] if match else None

# def extract_medicine_info(text):
#     """Extract medicine names and their strength from prescription text."""
#     words = text.split()  # Split the prescription into words
#     matched_medicines = []

#     for i in range(len(words)):
#         match = fuzzy_match(words[i])  # Match single words
#         if match:
#             # Check if the next word is a strength (e.g., "500mg")
#             if i < len(words) - 1 and re.match(r"\d+mg", words[i + 1]):
#                 match += " " + words[i + 1]
#             matched_medicines.append(match)

#     return list(set(matched_medicines))  # Remove duplicates
def extract_medicine_info(text):
    words = text.split()
    matched_medicines = []

    for i in range(len(words)):
        match = fuzzy_match(words[i], medicines_list)  # Pass medicines_list
        if match:
            if i < len(words) - 1 and re.match(r"\d+mg", words[i + 1]):
                match += " " + words[i + 1]
            matched_medicines.append(match)

    return list(set(matched_medicines))



# # Example usage
# if __name__ == "__main__":
#     sample_text = "amoxillin 500mg 2x a day for seven days"
#     detected_medicine = extract_medicine_info(sample_text)
#     print("Final Medicines Detected:", detected_medicine)
