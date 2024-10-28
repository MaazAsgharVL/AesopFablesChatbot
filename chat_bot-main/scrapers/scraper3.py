import os

# Path to your source file with all fables
source_file = 'a.txt'

# Folder to save individual fables
output_folder = '../data/scraper3'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to process the file and split it into individual fables
def process_fables(source_file):
    with open(source_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    fable_title = None
    fable_content = []
    empty_lines = 0

    for line in lines:
        # Check if the line is empty
        if line.strip() == '':
            empty_lines += 1
        else:
            # If there were 3 or more empty lines before this line, it's a heading
            if empty_lines >= 3:
                if fable_title and fable_content:
                    # Save the previous fable
                    save_fable(fable_title, fable_content)
                
                # Treat this line as the title of the next fable
                fable_title = line.strip()
                fable_content = []
            
            # Reset empty line counter and add line to the current fable content
            empty_lines = 0
            fable_content.append(line.strip())
    
    # Save the last fable if any content exists
    if fable_title and fable_content:
        save_fable(fable_title, fable_content)

# Function to save each fable into a separate file
def save_fable(title, content):
    file_name = title.replace(' ', '_').replace('/', '_') + '.txt'
    file_path = os.path.join(output_folder, file_name)
    
    # Check if the file already exists to avoid overwriting
    if os.path.exists(file_path):
        print(f"File {file_name} already exists. Skipping.")
        return
    
    with open(file_path, 'w', encoding='utf-8') as fable_file:
        fable_file.write('\n'.join(content))
    
    print(f"Saved fable: {title}")

# Run the process
process_fables(source_file)
