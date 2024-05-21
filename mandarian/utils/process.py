import re

def process_line(line):
    # 问题1和2: 删除中文文字和英文单词之间的多余空格
    line = re.sub(r'([\u4e00-\u9fa5])(\s+)([\u4e00-\u9fa5a-zA-Z])', r'\1\3', line)
    line = re.sub(r'([a-zA-Z])(\s+)([\u4e00-\u9fa5])', r'\1\3', line)

    # 问题3: 删除除编号外的中文和数字之间的多余空格
    line = re.sub(r'([\u4e00-\u9fa5])(\s+)(\d)', r'\1\3', line)
    line = re.sub(r'(\d)(\s+)([\u4e00-\u9fa5])', r'\1\3', line)

    return line

input_file_path = '/data/faster-whisper/mandarian/finaltext.txt'
output_file_path = '/data/faster-whisper/mandarian/processed_finaltext.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(output_file_path, 'w', encoding='utf-8') as file:
    for line in lines:
        processed_line = process_line(line.strip())
        file.write(processed_line + '\n')

print(f"处理后的文件已保存到：{output_file_path}")

