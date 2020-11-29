# Chapter 13 Challenges

# 1. Create Rectangle and Square classes with a method called calculate_perimeter
# that calculates the perimeter of the shapes they represent.
# Create Rectangle and Square objects and call the method on both of them

class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self,s):
        self.length = s

    def calculate_perimeter(self):
        return self.length * 4

    
rect = Rectangle(2,4)
print(rect.calculate_perimeter())

sq = Square(3)
side = sq.calculate_perimeter()
print(side)

# 2. Define a method in your Square class called 'change_size' that allows you to pass in a number
# that increases or decreases (if the number is negative) each side of a Square object by that number.

class Square:
    def __init__(self,s):
        self.length = s

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self,ch):
        self.length = self.length + ch

sqa = Square(5)
print(sqa.calculate_perimeter())
sqa.change_size(-2)
print(sqa.length)
print(sqa.calculate_perimeter())

# 3. Create a class called Shape. Define a method in it called 'what_am_i' that prints
# 'I am a shape' when called. Cahgne your Square and Rectangle classes from the previous
# challenges to inherit from Shape, Create Square and Rectangle objects,
# and call the new method on both of them.

class Shape:
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

sq_a = Square(4,4)
print(sq_a.what_am_i())

rec_a = Rectangle(3,2)
print(rec_a.what_am_i())

# 4. Create a class called Horse and a class called Rider.
# Use composition to model a horse that has a rider

class Horse:
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

class Rider:
    def __init__(self,name):
        self.name = name
    def rider_saying(self):
        print('Giddy Up')

dana = Rider('Dana')
my_horse = Horse('Brodie','horsebreed',dana)

print(my_horse.rider.rider_saying())
