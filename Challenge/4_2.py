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
    return print(r.text)


for i in range(128):
    char1='ss6'+chr(i)
    fuzzer(char1)

print("Good luck!")