
file_1=open("D:\99003785\DOC\input.txt","r")
file_output=open("file_example.txt","w")
print(file_1)
for each in file_1:
    print(each,end='')
    file_output.writelines(each)
