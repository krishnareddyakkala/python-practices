# python-practices
practice python tricks

# init_clean_weakref.py.py
Initialization and Cleanup with WeakValueDictionary

# singleton.py
Possibly the simplest design pattern is the singleton, which is a way to provide one and only one object of a particular type. To accomplish this, you must take control of object creation out of the hands of the programmer

# Decorators
This amazing feature appeared in the language almost apologetically and with concern that it might not be that useful.
I predict that in time it will be seen as one of the more powerful features in the language. The problem is that all the introductions to decorators that I have seen have been rather confusing, so I will try to rectify that here.
## Decorators vs. the Decorator Pattern
First, you need to understand that the word “decorator” was used with some trepidation in Python, because there was concern that it would be completely confused with the Decorator pattern from the Design Patterns book. At one point other terms were considered for the feature, but “decorator” seems to be the one that sticks.
Indeed, you can use Python decorators to implement the Decorator pattern, but that’s an extremely limited use of it. Python decorators, I think, are best equated to macros.
## What Can You Do With Decorators?
Decorators allow you to inject or modify code in functions or classes. Sounds a bit like Aspect-Oriented Programming (AOP) in Java, doesn’t it? Except that it’s both much simpler and (as a result) much more powerful. For example, suppose you’d like to do something at the entry and exit points of a function (such as perform some kind of security, tracing, locking, etc. – all the standard arguments for AOP).