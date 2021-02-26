#Author: Sourav Dey(99003785)
#Contact: sourav.dey@ltts.com /deysourav0909@gmail.com
#Date of creation: 22/2/2021

'''
This program performs the grep operation , i.e. user needs to provide a word that he / she wants to search
from the given file. The final output of the opeartion is a file is created with the count and instances of 
the desired word.
'''



import re

input_search_word_1=input("Enter the first word to be searched:\n")# User input; word to be searched by the user.
#pattern=re.compile(input_search_word_1,re.IGNORECASE)

file=open("D:\99003785\DOC\input.txt","r")# creation of the file
list_of_lines=[]
for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lines.append(line_list)
print(list_of_lines)


#function to calculate the number of words present in a file:
def Count_occurences(file):
    
    read_file1=file.read()
    z=(re.findall(input_search_word_1,read_file1,re.M|re.I))
    print(z)
    if z:
        return(len(z))
        
    else:
        print("The string entered does not match")



#capturing the occurences
a=Count_occurences(file)



#Creation of the file w.r.t the input given, function definition
def file_generate(input_word,occur) :
    if occur != 0:
        user_input_1=input_word+".txt"
        file_write=open(user_input_1,"w")
        file_write.write("The occurences are:"+str(occur))
        file_write.close()



#Function to create the file:
file_generate(input_search_word_1,a)

'''#Function to write lines in the file
def my_func(file):
    
    list_of_lines=[]
    for line in read_1:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lines.append(line_list)
    print(list_of_lines)






my_func(file)'''