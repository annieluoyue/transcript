import os
import re

def remove_punctuation(text):
    # 定义要去除的标点符号
    punctuation = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.'
    return ''.join(char for char in text if char not in punctuation)

input_dir = '/data/faster-whisper/mandarian/final_aishell2/simple_aishell2'

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = ' '.join(line.strip() for line in file)  # 去除换行符和行首空格

        content = remove_punctuation(content)  # 去除标点符号

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

