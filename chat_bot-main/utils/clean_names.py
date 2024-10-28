import os
import re

def clean_filenames(folder_path):
    # Regular expression to match only alphabets, underscores, spaces, and apostrophes
    pattern = re.compile(r"[^A-Za-z_' ]")  # Include apostrophes in the allowed characters

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Process only .txt files
        if filename.endswith('.txt'):
            # Remove everything except alphabets, underscores, spaces, and apostrophes from the filename
            cleaned_name = re.sub(pattern, '', filename.rsplit('.', 1)[0])
            
            # Replace '&' with 'and'
            cleaned_name = cleaned_name.replace('&', 'and')
            
            cleaned_name += '.txt'
            
            # Rename the file if the cleaned name is different
            if filename != cleaned_name:
                original_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, cleaned_name)
                os.rename(original_path, new_path)
                print(f"Renamed '{filename}' to '{cleaned_name}'")

# Specify the paths to the folders containing the .txt files
folder_paths = ["../data/scraper1", "../data/scraper2", "../data/scraper3", "../data/scraper4"]

for folder in folder_paths:
    clean_filenames(folder)