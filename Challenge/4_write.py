file1=open("4.txt",'w')
for i in range(128):
    char_1=chr(i)*4
    file1.write(char_1)
    file1.write('\n')
for i in range(125):
    char_1=chr(i)+chr(i+1)+chr(i+2)+chr(i+3)
    file1.write(char_1)
    file1.write('\n')
for i in range(3,128):
    char_1=chr(i)+chr(i-1)+chr(i-2)+chr(i-3)
    file1.write(char_1)
    file1.write('\n')
file1.close()