import os
import string

# 定义原始转录数据的目录
original_dir = "/data/faster-whisper/mandarian/aishell2tran"

# 定义处理后的转录数据存储目录
processed_dir = "/data/faster-whisper/mandarian/aishell2"

# 如果处理后的存储目录不存在，则创建该目录
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# 定义一个函数来移除文本中的标点符号
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# 遍历原始目录下的所有.txt文件
for filename in os.listdir(original_dir):
    if filename.endswith(".txt"):
        # 生成每个原始文件的完整路径
        original_file_path = os.path.join(original_dir, filename)
        # 生成每个处理后文件的存储路径
        processed_file_path = os.path.join(processed_dir, filename)

        # 读取原始文件内容
        with open(original_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 提取并保存不含标点的转录文本内容到新目录
        with open(processed_file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                # 分割每一行并提取文本部分
                text = line.split('] ')[1] if '] ' in line else line
                # 移除文本中的标点符号
                text_no_punctuation = remove_punctuation(text)
                # 写入处理后的文本
                file.write(f"{text_no_punctuation}\n")

