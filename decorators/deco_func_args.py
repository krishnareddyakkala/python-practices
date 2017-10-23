
# PythonDecorators/decorator_function_with_arguments.py
def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")

"""

Inside wrap()
After decoration
Preparing to call sayHello()
Inside wrapped_f()
Decorator arguments: hello world 42
sayHello arguments: say hello argument list
After f(*args)
after first sayHello() call
Inside wrapped_f()
Decorator arguments: hello world 42
sayHello arguments: a different set of arguments
After f(*args)
after second sayHello() call
The return value of the decorator function must be a function used to wrap the function to be decorated. 
That is, Python will take the returned function and call it at decoration time, passing the function to be decorated. 
That’s why we have three levels of functions; the inner one is the actual replacement function.

Because of closures, wrapped_f() has access to the decorator arguments arg1, arg2 and arg3, without having to 
explicitly store them as in the class version. However, this is a case where I find “explicit is better than implicit,” 
so even though the function version is more succinct I find the class version easier to understand and thus to modify 
and maintain.

"""