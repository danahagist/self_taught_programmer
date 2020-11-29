# Chapter 5 Challenges

# 1. Create a list of your favorite musicians
musician_list = ['Paul Simon', 'Bon Iver', '2 Pac']
print(musician_list)

# 2. Create a list of tuples, with each tuple containing the longitude and latitude
# of somewhere you've lived or visited

places_lived = [(100,120),(220,400),(400,500)]
print(places_lived)

# 3. Create a dictionary that contains different attributes about you:
# including: height, favorite_color, favorite_author, etc.

about_me = {'height':'5\'10\"',
            'color':'blue',
            'author':'vonnegut'}
print(about_me['height'])

# 4. Write a program that lets the user ask your height, favorite color, favorite author,
# and returns the result from the dictionary you created in the previous challenge

def user_question():
    x = input('Enter height, color, or author:')
    return about_me[x]
    print(about_me[x])

# 5. fav_songs = Create a dictionary mapping your favorite musicians
# to a list of your favorite songs by them

song_dict = {'Bon Iver':'Holocene',
             '2 Pac': 'Dear Mama',
             'Peter Gabriel':'Salisbury Hill'}

print(song_dict)


# 6 Python Sets:
# you could use a python set to store a set of things (maybe a grocery list),
# that doesn't need an order

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

