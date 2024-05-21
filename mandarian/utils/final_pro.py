import re

def process_line(line):
    # 确保编号和文本之间只有一个空格
    line = re.sub(r'(IC\d+)([^\s])', r'\1 \2', line)

    return line

input_file_path = '/data/faster-whisper/mandarian/processed_finaltext.txt'
output_file_path = '/data/faster-whisper/mandarian/final_processed_text.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(output_file_path, 'w', encoding='utf-8') as file:
    for line in lines:
        processed_line = process_line(line.strip())
        file.write(processed_line + '\n')

print(f"处理后的文件已保存到：{output_file_path}")

