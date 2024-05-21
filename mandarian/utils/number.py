# 指定原始 trans.txt 文件的路径
original_file_path = '/data/aishell2/iOS/data/trans.txt'

# 处理文件中的每一行，只保留编号
processed_lines = []
with open(original_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()  # 移除首尾空白并以空格分割字符串
        if len(parts) >= 1:  # 确保有编号部分
            processed_line = parts[0]  # 只取编号部分
            processed_lines.append(processed_line)

# 将处理后的内容写入新的 text 文件
new_file_path = '/data/faster-whisper/mandarian/number.txt'
with open(new_file_path, 'w', encoding='utf-8') as new_file:
    for processed_line in processed_lines:
        new_file.write(processed_line + '\n')

print(f"新的 text 文件已生成于路径：{new_file_path}")

