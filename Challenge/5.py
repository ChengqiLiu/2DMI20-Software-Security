import time
import os

main = "challenge_win.exe "
data="ACCESS DENIED\n"
_password="ilovefrogsandsecurity"
res=''
while(data == "ACCESS DENIED\n"):
    _password=_password+res
    time_list=[]
    for i in range(97,123):
        password=_password+chr(i)

        time_start=time.time()
        f=os.popen(main+password)
        data=(f.readlines())[0]
        f.close()
        time_end=time.time()

        t=time_end-time_start
        time_list.append(t)
        print(password)
        print(data)
        print(t)
        if(data != "ACCESS DENIED\n"):
            print(password)
            break
    _min=max(time_list)
    _id=time_list.index(_min)
    res=chr(_id+97)