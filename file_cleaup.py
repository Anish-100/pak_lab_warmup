
from pathlib import Path

max_len = 0

with open ('Warmup/data/Final attempt','r') as file:
        for line in file:
            length_of_line = len(line)
            max_len = max(length_of_line,max_len)

with open('Final_attempt_edited', 'w') as file_edited_file:
    with open ('Warmup/data/Final attempt','r') as file_2:
        for line in file_2:
            if line == '########\n':
                line = str('########'*int(max_len/8))
            if line == 'BREAK':
                continue
            file_edited_file.write(line)
            file_edited_file.write('\n')

             