# 1. Find a file on your computer and print its contents using python

import os
mypath = os.path.join('/','Library','Documentation')
with open(mypath+'/Warranty.txt','r') as f:
    print(f.read())

# 2. Write a program that asks a user a question, and saves their answer to a file.

with open('user_answer.txt','w') as f:
    a = input('What''s your favorite day of the year?')
    f.write(a)

with open('user_answer.txt','r') as f:
    print(f.read())


# 3. Take the items in this list of lists:
import csv

lol = [['Top Gun','Risky Business','Minority Report'] \
,['Titanic','The Revenant','Inception'] \
 ,['Training Day','Man on Fire','Flight']]

with open('movie.csv','w',newline = '') as f:
    w = csv.writer(f,delimiter = ',')
    for i in lol:
        w.writerow(i)


with open('movie.csv','r') as f:
    r = csv.reader(f, delimiter = ',')
    for row in r:
        print(','.join(row))

