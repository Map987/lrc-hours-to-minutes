import os

def convert_time(time_str):
    parts = time_str.split(':')
    if len(parts) < 3:
        return time_str 
    minutes = int(parts[0]) * 60 + int(parts[1])
    seconds, decimal = parts[2].split('.')
    return f"{minutes:02d}:{seconds}.{decimal}"

def process_lrc(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    part_number = 1
    current_minutes = 0
    total_minutes = 0  # 新增变量来跟踪总分钟数

    for line in lines:
        if '[' in line and ']' in line:
            time_str = line.split(']')[0][1:] 
            converted_time = convert_time(time_str)
            converted_time = converted_time[1:] if converted_time[:3].isdigit() and ":" not in converted_time[:3] else converted_time
            print(f"{converted_time}")
            current_minutes = int(converted_time.split(':')[0]) 
            total_minutes = current_minutes  # 更新总分钟数

            if total_minutes >= 100 * part_number:
                # 当总分钟数达到100的整数倍时，创建新的文件
                part_number += 1
                current_minutes = 0  
                
                base_file_name = os.path.basename(file_path)
                output_file_path = f"{os.path.dirname(file_path)}/{base_file_name.replace('.lrc', f'part{part_number}.txt')}"
                
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(f"[{converted_time}] {line.split(']')[1].strip()}\n")  
            else:
                base_file_name = os.path.basename(file_path)
                output_file_path = f"{os.path.dirname(file_path)}/{base_file_name.replace('.lrc', f'part{part_number}.txt')}"               
                with open(output_file_path, 'a', encoding='utf-8') as output_file:
                    output_file.write(f"[{converted_time}] {line.split(']')[1].strip()}\n")  
        else:
            output_file_path = f"{os.path.dirname(file_path)}/{base_file_name.replace('.lrc', f'part{part_number}.txt')}"
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.write(line.strip() + '\n')

process_lrc('/storage/emulated/0/Movies/【一週間限定特典つき】オ.lrc')