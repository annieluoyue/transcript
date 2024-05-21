import os

# 定义文件路径
number_file_path = '/data/faster-whisper/mandarian/number.txt'
input_dir = '/data/faster-whisper/mandarian/final_aishell2/simple_aishell2'
output_file_path = '/data/faster-whisper/mandarian/text.txt'

# 从number.txt读取编号
numbers = []
with open(number_file_path, 'r', encoding='utf-8') as file:
    numbers = [line.strip() for line in file]

# 对每个编号，读取对应的txt文件内容，并将编号和内容写入新文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for number in numbers:
        txt_file_path = os.path.join(input_dir, number + '.txt')
        try:
            with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                content = txt_file.read().strip()
                output_file.write(number + ' ' + content + '\n')
        except FileNotFoundError:
            print(f"文件 {txt_file_path} 不存在，跳过。")

print(f"文本文件已生成于：{output_file_path}")

