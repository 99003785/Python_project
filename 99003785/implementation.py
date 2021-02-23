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


#function to calculate the number of words present in a file:
def Count_occurences(file):
    count=0
    read_file1=file.read()

    z=(re.findall(input_search_word_1,read_file1,re.M|re.I))
    if z:
        return(len(z))

#capturing the occurences
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