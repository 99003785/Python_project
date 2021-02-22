#Author: Sourav Dey(99003785)
#Contact: sourav.dey@ltts.com /deysourav0909@gmail.com
#Date of creation: 22/2/2021

'''
This program performs the grep operation , i.e. user needs to provide a word that he / she wants to search
from the given file. The final output of the opeartion is a file is created with the count and instances of 
the desired word.

'''
import re
file=open("D:\99003785\DOC\input.txt","r")# creation of the file
input_search_word_1=input("Enter the first word to be searched:\n")# User input; word to be searched by the user.
count=0
read_file1=file.read()
z=(re.findall(input_search_word_1,read_file1,re.M|re.I))
if z:
    print(len(z))
read_file=file.readlines()
'''#Counting the number of times the word appears in the file.
for line in read_file:                                        
    z=(re.findall(input_search_word_1,file,re.M|re.I))
    if z:
        count+=1

#print(len(z))
print(count)'''
#Creation of the file where 
user_input_1=input_search_word_1+".txt"
file_write=open(user_input_1,"w")
file_write.write(str(len(z)))
file_write.close()

