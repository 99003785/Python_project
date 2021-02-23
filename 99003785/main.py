#Author: Sourav Dey(99003785)
#Contact: sourav.dey@ltts.com /deysourav0909@gmail.com
#Date of creation: 22/2/2021
import re

'''
This program performs the grep operation , i.e. user needs to provide a word that he / she wants to search
from the given file. The final output of the opeartion is a file is created with the count and instances of 
the desired word.

'''
'''import re
#Function to open the text file and take the user input

file=open("D:\99003785\DOC\input.txt","r")# creation of the file

input_search_word_1=input("Enter the first word to be searched:\n")# User input; word to be searched by the user.


#function to calculate the number of words present in a file:
def Count_occurences(file):
    count=0
    read_file1=file.read()

    z=(re.findall(input_search_word_1,read_file1,re.M|re.I))
    if z:
        return(len(z))

#read_file=file.readlines()
#Counting the number of times the word appears in the file.
for line in read_file:                                        
    z=(re.findall(input_search_word_1,file,re.M|re.I))
    if z:
        count+=1

#print(len(z))
print(count)
a=Count_occurences(file)

#Creation of the file w.r.t the input given, function definition
def file_generate(input_word,occur) :
    user_input_1=input_word+".txt"
    file_write=open(user_input_1,"w")
    file_write.write(str(occur))
    file_write.close()

#Opening input.txt

#Function to create the file:
file_generate(input_search_word_1,a)


#function to print lines
def func_to_print_lines(file):
    software=[]
    lines=0
    pattern=re.compile(input_search_word_1,re.IGNORECASE)
    for file_line in file:
        lines+=1
        if pattern.search(file_line) != None:
            software.append((lines,file_line.rstrip('\n')))
            print(software)
    for i in software:
        if pattern.search(software[i]):
            print(software[i-1]+software[i]+software[i+1])


#calling func to print the lines
func_to_print_lines(file)

'''

#with open("D:\99003785\DOC\input.txt") as searchfile:
with open("input.txt") as searchfile:
    text = searchfile.read()
    count=0
    for m in re.finditer('(?:^|\s+\S+) +gnu?(?:\s*\s+\S+|$)', text, re.IGNORECASE):
        print(m)
        

    

#([^\r\n]+) Software?([\r\n]| |$)
'''import re
pattern = "(.+)  software (.+) "
match = re.search(pattern, text)
if match:
    print(firstword_before = match.group(1) )# first pair of parentheses
    lastword_before = match.group(2)

    #firstword_after = match.group(3)
    #lastword_after = match.group(10)'''

