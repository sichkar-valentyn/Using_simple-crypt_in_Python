# File: Using_simple-crypt_in_Python.py
# Description: Using simple-crypt in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Using simple-crypt in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Using_simple-crypt_in_Python (date of access: XX.XX.XXXX)



# Implementing the task
# Importing the library simple-crypt
import simplecrypt

# Creating the list to save all lines from file p.txt
p = []

# Using loops for reading all lines in the file p.txt
# This file has lines with ten passwords
with open('p.txt') as inf:
    for line in inf:
        p += [line.strip()]


# Reading the data in binary form from file
with open('encrypted.bin', 'rb') as inf:
    s = inf.read()


# Trying to use all passwords to decrypt the information from the file
for i in range(len(p)):
    try:
        d = simplecrypt.decrypt(p[i], s)
    except:
        print('The password', i, 'was wrong')
    else:
        print('Password', i, 'is correct')
        print(d)
        break
