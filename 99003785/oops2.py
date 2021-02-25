import re
class python_project:

    def __init__(self, input_search_word):
        self.input_file = open("D:\99003785\DOC\input.txt")
        self.input_search_word=input_search_word
        self.file_line = self.input_file.read()
        
        print("I am in init func")

    def my_occur_func(self):
        count = 0
        str1 = " "
        file_name = input_search_word+".txt" #For output file
        file_out = open(file_name, 'w')
        file_list = self.file_line.split()
        file_1 = re.split(r"\W",str(file_list))
        x=list(filter(None,file_1))
        for i in range(len(x)):
            match = re.fullmatch(self.input_search_word, x[i], re.M|re.I)
            if match:
                count += 1
                str1 = x[i-1]+" "+x[i]+" "+x[i+1]
                file_out.write(str1)
                file_out.write("\n")

        print(count)
        file_out.write("Number of occurences="+str(count))
        self.input_file.close()
        file_out.close()


if __name__ == "__main__":
    number=int(input("Enter the number of words you want to search:\n"))
    while number!=0:
        input_search_word=input("Enter the word:\n")
        word = python_project(input_search_word)
        word.my_occur_func()
        number-=1
