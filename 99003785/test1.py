import re
count = 0
str1 = " "
input_file = open("D:\99003785\DOC\input.txt")
input_word_searched = input("Enter the word:\n")
file_name = input_word_searched+".txt" #For output file
file_out = open(file_name, 'w')

file_line = input_file.read()
#file_3 = [file_line.strip(' ') for x in file_line]
#file__2=''.join(file_line.split())
file_list = file_line.split()
file_1 = re.split(r"\W",str(file_list))
x=list(filter(None,file_1))

#filer_1 = re.sub('+',' ',file_1)



for i in range(len(x)):
    match = re.fullmatch(input_word_searched, x[i], re.M|re.I)
    if match:
        count += 1
        str1 = x[i-1]+" "+x[i]+" "+x[i+1]
        file_out.write(str1)
        file_out.write("\n")

print(count)
file_out.write("Number of occurences="+str(count))
input_file.close()
file_out.close()


