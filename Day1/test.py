import re
count= 0
software=list()
lines=0
list_of_lines=[]
pattern=re.compile("Software",re.IGNORECASE)

with open("D:\99003785\DOC\input.txt",'rt') as file_info:

    for file_line in file_info:
        lines+=1
        
        if pattern.search(file_line)!= None:
            software.append((lines,file_line.rstrip('\n')))
           ''' for line in software:
                stripped_line = line.strip()
                line_list = stripped_line.split()
                list_of_lines.append(line_list)
        print(list_of_lines)'''

                            
    for answer in software:
        count+=1
        
        with open("software.txt",'a') as file_answer:
            file_answer.writelines(str(count)+':')
            file_answer.writelines(answer[1]+'\n')        

