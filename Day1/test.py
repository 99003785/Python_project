import re
count= 0
software=[]
lines=0

pattern=re.compile("Software",re.IGNORECASE)

with open("D:\99003785\DOC\input.txt",'rt') as file_info:

    for file_line in file_info:
        lines+=1
        
        if pattern.search(file_line)!= None:
            software.append((lines,file_line.rstrip('\n')))

                
    for answer in software:
        count+=1
        print(answer[1]+'\n')
        for word in answer:
            print(word)
        


        with open("software.txt",'a') as file_answer:
            file_answer.writelines(str(count)+':')
            file_answer.writelines(answer[1]+'\n')        

