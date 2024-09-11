file1=open("4.txt",'r')
l=[]
while(True):
    str1=file1.read(5)[0:4]
    if str1=='':
        break
    l.append(str1)