# 1. Print every charater in the string 'Camus.'
for i in 'Camus':
    print(i)

    
# 2. Write a program that collects two strings from a user,
# inserts them into the string
# 'Yesterday I wrote a [response_one]. I sent it to [response_two]!"

#response_one = input("What did you write?")
#response_two = input("Who did you send it to?")
#print("Yesterday I wrote a {}. I sent it to {}!".format(response_one,response_two))
                     
# 3. Use a method to make the string 'aldous Huxley was born in 1984.'
# gramatically correct by capitalizaing the first letter in the sentence
aldous_string = 'aldous Huxley was born in 1894.'
aldous_string = aldous_string[0].upper() + aldous_string[1:]
print(aldous_string)


# 4. "Where now? Who now? When now?" and return a list that looks like
# ['Where now?, Who now? When now?']
lst = "Where now? Who now? When now?".split("?")
newlst = []
print(newlst)
for i in lst:
	newlst.append(i+'?')

newlst = newlst[:3]
print(newlst)

# 5. Take the list ['The', 'fox','jumped','over','the','fence','.']
# and turn it into a grammatically correct string. There should be a space between each word,
# but no space between the word fence and the period that follows it.

a = ['The','fox','jumped','over','the','fence','.']
foxlst = ' '.join(a)
print(foxlst.replace(' .','.'))

# 6. Replace every instance of 's' in 'A screaming comes across the sky.'
# with a dollar sign

scr = 'A screaming comes across the sky.'
scr = scr.replace('s','$')
print(scr)


# 7. Use a method to find the first index of the character 'm' in the string 'Hemingway'.
m_index = 'Hemingway'.index('m')
print(m_index)


# 8. Find dialogue in your favorite book (containing quotes) and turn it into a string.
nice_quote = 'It\'s not the years in your life, but the life in your years.'
print(nice_quote)

# 9. Create the string 'three three three' using concatenation, and then again using multiplication.
print('three ' + 'three ' + 'three')
print('three ' * 3)

# 10. Slice the string 'It was a bright cold day in April, and the clocks were striking thirteen.'
# to only include the characters before the comma.

ten_str = 'It was a bright cold day in April, and the clocks were striking thirteen.'
ten_str = ten_str.split(',')[0]
print(ten_str)

