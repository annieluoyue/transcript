import os
import re

def process_line(line):
    # 检查并插入空格以分隔编号和文本
    line = re.sub(r'^(.{11})([^\s])', r'\1 \2', line)

    # 去除标点符号（您之前的代码已经包含）
    punctuation = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.'
    line = ''.join(char for char in line if char not in punctuation)

    return line

input_file_path = '/data/faster-whisper/mandarian/finaltext.txt'
output_file_path = '/data/faster-whisper/mandarian/new_processed_finaltext.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in lines:
        processed_line = process_line(line.strip())
        output_file.write(processed_line + '\n')

print(f"处理后的文件已保存到：{output_file_path}")

