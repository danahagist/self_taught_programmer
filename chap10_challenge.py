''' Chapter 10 Challenges '''
# 1. Define a class called Apple with four instance variables that represent apple attributes.

class Apple:
    def __init__(self,w,c,k,s):
        self.weight = w
        self.color = c
        self.kind = k
        self.sour = s

        
# 2. Create a Circle class with a method called area that calculates and returns its area.
# Then create a Cicle object, call area on it, and print the result.
# Use Python's pi function in the built in math module.

import math
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return math.pi * self.radius**2


# 3. Create a Triangle class with a method called area that calculates and returns its area.
# Then create a Triangle object, call area on it, and print the result.

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def area(self):
        return 1/2 * self.base * self.height

    
# 4. Make a Hexagon class with a method called calculate_perimeter that calculates and returns its perimiter.
# Then create a Hexagon object, call calculate_perimiter on it, and print the result.

class Hexagon:
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6
    
    
