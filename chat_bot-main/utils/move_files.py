import os
import shutil

def move_txt_files(source_folders, destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Set to track moved filenames to avoid duplicates
    moved_files = set()

    for folder in source_folders:
        # Iterate through each file in the folder
        for filename in os.listdir(folder):
            if filename.endswith('.txt'):
                # Construct the full file path
                source_file_path = os.path.join(folder, filename)
                destination_file_path = os.path.join(destination_folder, filename)

                # Check if the file already exists in the destination
                if filename not in moved_files and not os.path.exists(destination_file_path):
                    # Move the file
                    shutil.move(source_file_path, destination_file_path)
                    moved_files.add(filename)
                    print(f"Moved '{filename}' to '{destination_folder}'")

    # Remove the source folders after moving files
    for folder in source_folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)  # Remove the folder and its contents
            print(f"Removed folder '{folder}'")

# Specify the path to the main data folder and the source folders
data_folder = 'data'
source_folders = [
    os.path.join(data_folder, 'scraper1'),
    os.path.join(data_folder, 'scraper2'),
    os.path.join(data_folder, 'scraper3'),
    os.path.join(data_folder, 'scraper4')
]

# Specify the destination folder
destination_folder = os.path.join(data_folder, 'raw_data')

# Move the .txt files
move_txt_files(source_folders, destination_folder)