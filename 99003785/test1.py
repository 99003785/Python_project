import re
count = 0
str1 = " "
file_inp_1 = open("input.txt")
word_searched = input("Enter the word:\n")
file_line = file_inp_1.read()
file_list = file_line.split()
file_name = word_searched+"txt"
file_out = open(file_name, 'w')

for i in range(len(file_list)):
    match = re.match(word_searched, file_list[i], re.M|re.I)
    if match:
        count += 1
        str1 = file_list[i-1]+" "+file_list[i]+" "+file_list[i+1]
        file_out.write(str1)
        file_out.write("\n")

print(count)
file_out.write("count="+str(count))
file_inp_1.close()
file_out.close()


