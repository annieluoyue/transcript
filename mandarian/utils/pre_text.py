# Path to the tran.txt file
tran_txt_path = '/data/faster-whisper/mandarian/utils/trans.txt'  # Update this path to the actual path of your tran.txt file

# Reading the file, modifying the lines, and writing them to a new file
with open(tran_txt_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    parts = line.strip().split('\t')  # Splitting by tab character
    if len(parts) == 2:
        audio_id, content = parts
        new_line = f"{audio_id} {content}\n"
        new_lines.append(new_line)

# Writing the modified lines back to the file
with open(tran_txt_path, 'w', encoding='utf-8') as file:
    file.writelines(new_lines)

print("The tran.txt file has been modified as requested.")

