

import re


#function to calculate the number of words present in a file:
def Count_occurences(file,pattern):
    count=0
    read_file1=file.read()

    z=(re.findall(pattern,read_file1,re.M|re.I))
    if z:
        return(len(z))
    else:
        print("The string entered does not match")



#Creation of the file w.r.t the input given, function definition
def file_generate(input_word,occur) :
    if occur != 0:
        user_input_1=input_word+".txt"
        file_write=open(user_input_1,"w")
        file_write.write(str(occur))
        file_write.close()




if __name__=="__main__":
    
    input_search_word_1=input("Enter the first word to be searched:\n")# User input; word to be searched by the user.
    file=open("D:\99003785\DOC\input.txt","r")# creation of the file
    #capturing the occurences
    a=Count_occurences(file,input_search_word_1)

    #Function to create the file:
    file_generate(input_search_word_1,a)