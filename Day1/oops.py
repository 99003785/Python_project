import re
class python_project():

    #def __init__(self):
        #self.search_word_1 = input("Enter the first word to be searched.\n")
        #self.search_word_2 = input("Enter the second word to be searched.\n")

    def __int__(self,word):
        self.input_word = word
        self.file = open("D:\99003785\DOC\input.txt")
        self.file_read = self.file.read()
        self.count=0
        #self.input_word = input_word
        self.file_o_word = self.str(self.input_word)+".txt"
        self.file_output = open("file_output",'w')
        self.file_list = self.file_read.split()
        self.file_1 = re.split(r"\W",str(self.file_list))
        self.x=list(filter(None,self.file_1))
        for i in range(len(self.x)):
            self.match = self.re.fullmatch(self.input_word, self.x[i], self.re.M|self.re.I)
        if self.match:
            self.count += 1
            str1 = self.x[i-1]+" "+self.x[i]+" "+self.x[i+1]
            self.file_output.write(str1)
            self.file_output.write("\n")

        print(self.count)
        self.file_output.write("Number of occurences="+str(self.count))

    '''#def my_occur_check(self):
        self.file_list = self.file_read.split()
        self.file_1 = re.split(r"\W",str(self.file_list))
        self.x=list(filter(None,self.file_1))
        for i in range(len(self.x)):
            self.match = self.re.fullmatch(self.input_word, self.x[i], self.re.M|self.re.I)
        if self.match:
            self.count += 1
            str1 = self.x[i-1]+" "+self.x[i]+" "+self.x[i+1]
            self.file_output.write(str1)
            self.file_output.write("\n")

        print(self.count)
        self.file_output.write("Number of occurences="+str(self.count))'''

    def my_func_closing_file(self):
        self.file.close()
        self.file_output.close()



    '''@classmethod
    def my_func_get_user_input(self):
        self.input_search_word=input("Enter the word to be searched:\n")'''







    
        #list_of_keywords=[]
#n=int(input("Enter the number of words you want to search:\n"))
n=input("Enter the word to be searched:\n")
word = python_project()

#word.my_occur_check()
#word.my_func_closing_file()
#for i in range(n):
#word = python_project.my_func_get_user_input()


            #input_search_word=input("Enter the word to be searched:\n")

