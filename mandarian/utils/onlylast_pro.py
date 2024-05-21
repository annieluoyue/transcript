import re

def process_line(line):
    # 删除中文文字之间的多余空格
    line = re.sub(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])', r'\1\2', line)

    # 删除中文字符和英文单词之间的多余空格
    line = re.sub(r'([\u4e00-\u9fa5])\s+([a-zA-Z])', r'\1\2', line)
    line = re.sub(r'([a-zA-Z])\s+([\u4e00-\u9fa5])', r'\1\2', line)

    # 删除除编号外的中文和数字之间的多余空格
    line = re.sub(r'([\u4e00-\u9fa5])\s+(\d)', r'\1\2', line)
    line = re.sub(r'(\d)\s+([\u4e00-\u9fa5])', r'\1\2', line)

    # 删除英文单词和数字之间的多余空格
    line = re.sub(r'([a-zA-Z])\s+(\d)', r'\1\2', line)
    line = re.sub(r'(\d)\s+([a-zA-Z])', r'\1\2', line)

    # 确保英文单词之间只有一个空格
    line = re.sub(r'([a-zA-Z])\s+([a-zA-Z])', r'\1 \2', line)

    # 确保编号和文本之间有一个空格
    line = re.sub(r'^(.{11})([^\s])', r'\1 \2', line)

    return line

input_file_path = '/data/faster-whisper/mandarian/new_processed_finaltext.txt'
output_file_path = '/data/faster-whisper/mandarian/onlylast_processed_finaltext.txt'


with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in lines:
        processed_line = process_line(line.strip())
        output_file.write(processed_line + '\n')

print(f"处理后的文件已保存到：{output_file_path}")

