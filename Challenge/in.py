import struct
list_d=[]
for i in range(31):
    list_d.append(0x30)
list_d2=[0x78,0x4f,0x6b,0x00]
list_d=list_d+list_d2
with open('in.txt','wb') as fp:
        for x in list_d:
                a=struct.pack('B',x)
                fp.write(a)
print('done')