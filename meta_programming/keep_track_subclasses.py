"""
Self-Registration of Subclasses
It is sometimes convienient to use inheritance as an organizing mechanism – each sublclass becomes an element of a 
group that you work on. For example, in CodeManager.py in the Comprehensions chapter, the subclasses of Language were 
all the languages that needed to be processed. Each Language subclass described specific processing traits for that 
language.

To solve this problem, consider a system that automatically keeps a list of all of its “leaf” subclasses 
(only the classes that have no inheritors). 
This way we can easily enumerate through all the subtypes:
"""
# Metaprogramming/RegisterLeafClasses.py

class RegisterLeafClasses(type):
    def __init__(cls, name, bases, nmspc):
        super(RegisterLeafClasses, cls).__init__(name, bases, nmspc)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        cls.registry.add(cls)
        cls.registry -= set(bases) # Remove base classes
    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)
    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])

class Color(object):
    __metaclass__ = RegisterLeafClasses

class Blue(Color): pass
class Red(Color): pass
class Green(Color): pass
class Yellow(Color): pass
print(Color)
class PhthaloBlue(Blue): pass
class CeruleanBlue(Blue): pass
print(Color)
for c in Color: # Iterate over subclasses
    print(c)

class Shape(object):
    __metaclass__ = RegisterLeafClasses

class Round(Shape): pass
class Square(Shape): pass
class Triangular(Shape): pass
class Boxy(Shape): pass
print(Shape)
class Circle(Round): pass
class Ellipse(Round): pass
print(Shape)

""" Output:
Color: Red, Blue, Green, Yellow
Color: Red, CeruleanBlue, Green, PhthaloBlue, Yellow
Red
CeruleanBlue
Green
PhthaloBlue
Yellow
Shape: Square, Round, Boxy, Triangular
Shape: Square, Ellipse, Circle, Boxy, Triangular
"""

"""
Two separate tests are used to show that the registries are independent of each other. Each test shows what happens 
when another level of leaf classes are added – the former leaf becomes a base class, and so is removed from the 
registry.

This also introduces metamethods, which are defined in the metaclass so that they become methods of the class. 
That is, you call them on the class rather than object instances, and their first argument is the class object rather 
than self.
"""