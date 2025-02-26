import pandas as pd

# Load the medicine dataset
csv_path = "./az-medicine-dataset-of-india/A_Z_medicines_dataset_of_India.csv"  # Update this if needed
df = pd.read_csv(csv_path)

# Extract medicine names (assuming the column name is 'Medicine_Name')
medicine_column = "short_composition1"  # Change if the column has a different name
if medicine_column not in df.columns:
    print(f"⚠️ Column '{medicine_column}' not found. Available columns: {df.columns}")
else:
    # Assign default frequency (higher values make the word more likely to be suggested)
    df["Frequency"] = 1000  

    # Save as a text file in SymSpell format
    dictionary_path = "./data/medical_dictionary.txt"
    df[[medicine_column, "Frequency"]].to_csv(dictionary_path, sep="\t", index=False, header=False)
    
    print(f"✅ Medical dictionary saved at {dictionary_path}")
