# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

with open ('amazon/train.neg', 'rb') as file:
    text = file.readlines()
    
print(text[:10])

print(text[0].decode().split(' '))

with open ('amazon/amazon_new/train.neg', 'wb') as file2:
    for line in text:
        if len(line.decode().split(' ')[:-1])<=14:
            file2.write(line)
