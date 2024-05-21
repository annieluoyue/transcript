# 指定原始文件和最终文件的路径
original_file_path = '/data/faster-whisper/mandarian/text.txt'
final_file_path = '/data/faster-whisper/mandarian/finaltext.txt'

# 读取原始文件
with open(original_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 去除所有的“。”符号
content = content.replace('。', '').replace('《', '').replace('·', '')

# 将处理后的内容写入新文件
with open(final_file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"处理后的文本已保存到：{final_file_path}")

