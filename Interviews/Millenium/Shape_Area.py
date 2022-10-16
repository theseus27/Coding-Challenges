#Passed all tests

import math
class Circle:
    radius = 0
    def __init__(self, r):
         self.radius = float(r)
    def getArea(self):
        return math.ceil(3.14159265 * self.radius * self.radius)

class Rectangle:
    length = 0
    width = 0
    def __init__(self, l, w):
        self.length = float(l)
        self.width = float(w)
    def getArea(self):
        return math.ceil(self.length * self.width)
    
class Square:
    width = 0
    def __init__(self, w):
        self.width = float(w)
    def getArea(self):
        return math.ceil(self.width * self.width)