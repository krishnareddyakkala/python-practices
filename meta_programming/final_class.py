"""
Making a Class “Final”
It is sometimes convenient to prevent a class from being inherited:
"""
# Metaprogramming/Final.py
# Emulating Java's 'final'

class final(type):
    def __init__(cls, name, bases, namespace):
        super(final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, final):
                raise TypeError(str(klass.__name__) + " is final")

class A(object):
    pass

class B(A):
    __metaclass__= final

print( B.__bases__)
print(isinstance(B, final))

# Produces compile-time error:
class C(B):
    pass

""" Output:
(<class '__main__.A'>,)
True
...
TypeError: B is final
"""

"""
During class object creation, we check to see if any of the bases are derived from final. Notice that using a metaclass 
makes the new type an instance of that metaclass, even though the metaclass doesn’t show up in the base-class list.

Because this process of checking for finality must be installed to happen as the subclasses are created, rather than 
afterwards as performed by class decorators, it appears that this is an example of something that requires metaclasses 
and can’t be accomplished with class decorators.
"""
