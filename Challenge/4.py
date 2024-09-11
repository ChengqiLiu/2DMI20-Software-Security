#!/usr/bin/env python3
import sys, requests, re, random, os
from requests.auth import HTTPDigestAuth
import time

##### Don't forget to fill in your password #####
url, auth = 'http://131.155.23.143:8843', HTTPDigestAuth('1954148', 'RIXE4RGF')
sid, token = '1954148', '63e8897d1720ef2dd7488e27b78a5684cd9cf7db'

req = requests.Session()
req.cookies['token'] = token

r = req.get(url+'/', auth=auth)

##### Validate your password using the check_input function #####
def check_input(fuzz):
    r = req.post(url+'/check_input', auth=auth, data={'fuzz': fuzz, 'fmt': 'txt'})
    return print(r.text)

##### For fuzzer: input either a string or a list of strings. The strings should consist of ASCII characters #####
def fuzzer(test):
    r = req.post(url+'/fuzzer', auth=auth, data={'test': test, 'fmt': 'txt'})
    if(r.text[6:10]!='This'):
        print("!!!!!!!!!!!!!!!!!!!")
    print(r.text)
    return 


file1=open("4.txt",'r+')
l=[]
while(True):
    str1=file1.read(5)[0:4]
    if str1=='':
        break
    l.append(str1)
str1='0000'
for j in range(100):
    while(str1 in l):
        char1=''
        for i in range(4):
            char1=char1+chr(random.randint(33,126))
        str1=char1
    l.append(str1)
    file1.write(str1+'\n')
    fuzzer(str1)

file1.close()

print("Good luck!")