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
