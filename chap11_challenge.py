# Chapter 11 Challenges
# 1. add a square_list calss variable to a class called Square so that every time you create
# a new Square object, the new object gets added to the list

class Square:
    sq_list = []
    def __init__(self,s):
        self.side = s
        self.sq_list.append(self.side)

sq1 = Square(4)
sq2 = Square(3)
sq3 = Square(5)
print(Square.sq_list)




# 2. Change the Square class so that when you print a Square object, a message prints telling
# you the len of each of the four sides of the shape. For example, if you create a square with
# Square(29) and print it, Python should print '29 by 29 by 29 by 29.

class Square:
    sq_list = []
    def __init__(self,s):
        self.side = s
        self.sq_list.append(self.side)

    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.side,self.side,self.side,self.side)

sq4 = Square(6)
print(sq4)

# 3. Write a function that takes two objects as parameters and returns True
# if they are the same object, and False if not.

def is_same(obj_a,obj_b):
    if obj_a == obj_b:
        return True
    else:
        return False





