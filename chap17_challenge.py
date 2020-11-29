#zen = open("/Users/dhagist/self_taught_programmer/zen.txt","r").read()
#print(zen.read())

with open("/Users/dhagist/self_taught_programmer/zen.txt","r") as zen:
    zen = zen.read()

import re

#1. Write a regular expression that matches the word Ducth in The Zen of Python
dutch = re.findall('Dutch',zen,re.MULTILINE)
print(dutch)

#2 Come up with a regular expression that matches all the digits in the string
# Arizona, 479, 501, 870. California 209, 213, 650
dig_string =  'Arizona, 479, 501, 870. California 209, 213, 650'
digits = re.findall("\d",dig_string)
print(digits)


#3 Create a regular expression that matches any word that starts with any character and is
# followed by two o's Then use Python's re module to match boo and loo in the sentence
# The ghost that says boo haunts the loo
oo_str = "The ghost that says boo haunts the loo"
any_char = re.findall('.oo',oo_str)
print(any_char)
