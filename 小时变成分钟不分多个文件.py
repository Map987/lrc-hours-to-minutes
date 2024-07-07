import os

def convert_time(time_str):
    parts = time_str.split(':')
    if len(parts) < 3:
        return time_str 
    minutes = int(parts[0]) * 60 + int(parts[1])
    seconds, decimal = parts[2].split('.')
    return f"{minutes:02d}:{seconds}.{decimal}"

def process_lrc(file_path):
    # 读取源文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 创建一个临时列表来存储修改后的行
    modified_lines = []

    for line in lines:
        if '[' in line and ']' in line:
            time_str = line.split(']')[0][1:] 
            converted_time = convert_time(time_str)
            
            # 修改时间戳并添加到修改后的行列表中
            modified_lines.append(f"[{converted_time}] {line.split(']')[1].strip()}\n")
        else:
            # 如果行没有时间戳，直接添加到修改后的行列表中
            modified_lines.append(line.strip() + '\n')

    # 将修改后的行写回源文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

    print(f"已保存到源文件: {file_path}")

# 处理文件
process_lrc('/content/ok.lrc')
