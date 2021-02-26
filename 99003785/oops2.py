# Author: Sourav Dey (99003785)
# Contact: sourav.dey@ltts.com /deysourav0909@gmail.com
# Date of creation: 22/2/2021

# -------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------#

"""
This program performs the grep operation i.e. user needs to
provide a word that he / she wants to search
from the given file.
The final output of the operation is a file is created
with the count and instances of
the desired word.
"""

# -------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------#

import re

# -------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------#
'''
This block contains the class PythonProject.
All the file related operation like opening a file and
passing the input search word is passed
in the init constructor of the class.

'''
# --------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------#


class PythonProject:

    def __init__(self, input_search):
        self.input_file = open("D:\99003785\DOC\input.txt", 'r')
        self.input_search = input_search
        self.file_line = self.input_file.read()
        print("I am in init func")

        # -----------------------------------------------------------------------------------------------#
        '''
        This method performs the grep operation.
        It searches the word in the file and returns the occurrences
        and its instances.
        '''
        # -----------------------------------------------------------------------------------------------#


class MyOperation(PythonProject):

    def my_occur_func(self):
        count = 0
        # str1 = " "
        file_name = input_search_word+".txt"  # For output file
        file_out = open(file_name, 'w')
        file_list = self.file_line.split()
        file_1 = re.split(r"\W", str(file_list))
        x = list(filter(None, file_1))
        for i in range(len(x)):
            match = re.fullmatch(self.input_search, x[i], re.M | re.I)
            if match:
                count += 1
                str1 = x[i-1]+" "+x[i]+" "+x[i+1]
                file_out.write(str1)
                file_out.write("\n")

        print(count)
        file_out.write("Number of occurrences ="+str(count))
        self.input_file.close()
        file_out.close()

# ------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------#


'''
This is the main function.
It takes the user input.
The object of the above defined class is created in the main function.
'''


# ------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    number = int(input("Enter the number of words you want to search:\n"))
    while number != 0:
        input_search_word = input("Enter the word:\n")
        word = MyOperation(input_search_word)
        word.my_occur_func()
        number -= 1
