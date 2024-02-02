import os

def convert_time(time_str):
    # 分割输入的时间字符串
    parts = time_str.split(':')
    
    # 检查是否有足够的部分
    if len(parts) < 3:
        return time_str  # 如果输入不符合格式，则保持原样
    
    # 将小时转换为分钟并转换为整数
    minutes = int(parts[0]) * 60 + int(parts[1])
    
    # 获取秒和小数部分
    seconds, decimal = parts[2].split('.')
    
    # 输出转换后的时间字符串
    return f"{minutes:02d}:{seconds}.{decimal}"

def process_lrc(file_path):
    # 读取txt文件
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 逐行处理并输出到新的txt文件
    part_number = 1
    current_minutes = 0
    for line in lines:
        # 检查行是否包含时间字符串
        if '[' in line and ']' in line:
            time_str = line.split(']')[0][1:]  # 提取时间部分
            converted_time = convert_time(time_str)
            current_minutes = int(converted_time.split(':')[0]) 
            
            # 如果当前分钟数达到一个新的100分钟部分，创建新文件
            if current_minutes - int(part_number) >= 100:
                part_number += 1
                current_minutes = 0  # 重置当前分钟数为下一部分的起始
                base_file_name = os.path.basename(file_path)  # 获取输入文件的基名
                output_file_path = f"{os.path.dirname(file_path)}/{base_file_name.replace('.lrc', f'part{part_number}.txt')}"
                
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(f"[{converted_time}] {line.split(']')[1].strip()}\n")  # 写入处理后的时间和文本
            else:
                # 否则，继续在当前文件中写入  
                base_file_name = os.path.basename(file_path)  # 获取输入文件的基名
                output_file_path = f"{os.path.dirname(file_path)}/{base_file_name.replace('.lrc', f'part{part_number}.txt')}"
                
                with open(output_file_path, 'a', encoding='utf-8') as output_file:
                    output_file.write(f"[{converted_time}] {line.split(']')[1].strip()}\n")  # 写入处理后的时间和文本
        else:
            # 如果行不包含时间字符串，原样写入
            output_file_path = f"{os.path.dirname(file_path)}/{base_file_name.replace('.lrc', f'part{part_number}.txt')}"
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.write(line.strip() + '\n')

# 调用函数处理LRC文件
process_lrc('/storage/emulated/0/111/测试.lrc')
