import re
count = 0
str1 = " "
input_file = open("D:\99003785\DOC\input.txt")
input_word_searched = input("Enter the word:\n")
file_name = input_word_searched+"txt"
file_out = open(file_name, 'w')
file_line = input_file.read()
file_list = file_line.split()
file_1 = re.split(r"\W",str(file_list))


for i in range(len(file_1)):
    match = re.fullmatch(input_word_searched, file_1[i], re.M|re.I)
    if match:
        count += 1
        str1 = file_1[i-4]+" "+file_1[i]+" "+file_1[i+4]
        file_out.write(str1)
        file_out.write("\n")

print(count)
file_out.write("count="+str(count))
input_file.close()
file_out.close()


