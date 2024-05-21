import os
from opencc import OpenCC

# Directory paths
source_dir = '/data/faster-whisper/mandarian/aishell2'  # Source directory
target_dir = '/data/faster-whisper/mandarian/simple_aishell2'  # Target directory

# Create the target directory if it does not exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Initialize the OpenCC converter for traditional to simplified Chinese
converter = OpenCC('t2s')

# Function to convert traditional Chinese to simplified Chinese in a file
def convert_file(file_path, target_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        simplified_content = converter.convert(content)
    
    with open(target_path, 'w', encoding='utf-8') as file:
        file.write(simplified_content)

# Process each txt file in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        source_file_path = os.path.join(source_dir, filename)
        target_file_path = os.path.join(target_dir, filename)
        convert_file(source_file_path, target_file_path)

print("Files have been converted and saved in the specified directory.")

