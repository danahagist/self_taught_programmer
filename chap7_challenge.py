# 1. Print each item in the following list: ['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']
show_list = ['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']
for i in show_list:
    print(i)

# 2. Print all the numbers from 25 to 50
for i in range(25,51):
    print(i)

    
# 3. Print each item in the list from the first challenge and their indexes
for i, show in enumerate(show_list):
    print(str(i) + ':' + show)

# 4. Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers. Each time through the loop ask the user to guess a number
# on the list and tell them whether or not they guessed correctly.

numlst = [1,18,27,42]
while True:
    a = input('guess a number:')
    if a == 'q':
        break
    if int(a) in numlst:
        print('you guessed it, now get outta here!')
        break


# 5. Multiply all the numbers in the list [8,19,148,4] with all the numbers in the list
# [9,1,33,83] and append each result to a third list

first_list = [8,9,148,4]
second_list = [9,1,33,83]
third_list = list()
for i in first_list:
    for j in second_list:
        a = i * j
        third_list.append(a)

print(third_list)
