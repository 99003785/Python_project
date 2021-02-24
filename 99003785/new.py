import re
input_1=input("Enter the word:\n")
file=open("D:\99003785\DOC\input.txt",'r')

count=1
read_line=file.readlines()
for line in read_line():
    list_1=re.findall(input_1,line,re.M|re.I)
    if list_1:
        count+=1

print(count)