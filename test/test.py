import os
import re

with open('a.txt', encoding='utf-8') as f:
    lines = f.readlines()
    # print(lines)
    dir_path = ''
    dir_path2 = ''
    for line in lines:
        print(line.strip())
        line = line.strip()
        if re.search('^## ', line):
            dir_path = f'./PyAutoGUI/0{line[3:]}'
            os.mkdir(dir_path)
        if re.search('^### ', line):
            chapter_section = f'0{line[4:7].replace(".", "0")}'
            dir_path2 = f'{dir_path}/{chapter_section}{line[7:]}'
            os.mkdir(dir_path2)
        if re.search('- ', line):
            file_path = f'{dir_path2}/{line[2:]}'
            with open(file_path, 'w') as f:
                pass
