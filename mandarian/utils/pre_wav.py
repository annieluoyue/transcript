# Corrected path to the wav.scp file
wav_scp_path = '/data/faster-whisper/mandarian/utils/wav.scp'  # Update this with the correct path

# Prefix to add to each audio path
prefix = '/data/aishell2/iOS/data/'

# Read, modify, and write back to the wav.scp file
with open(wav_scp_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        audio_id, audio_path = parts
        new_line = f"{audio_id} {prefix}{audio_path}\n"
        new_lines.append(new_line)

# Writing the modified lines back to the file
with open(wav_scp_path, 'w', encoding='utf-8') as file:
    file.writelines(new_lines)

print("The wav.scp file has been modified as requested.")

