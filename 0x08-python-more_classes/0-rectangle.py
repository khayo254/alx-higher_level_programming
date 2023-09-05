#!/usr/bin/python3
class Rectangle:
    pass
def __init__(self, name):
    self.name = name
def __str__(self):
    return f"{self.name}"
my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
