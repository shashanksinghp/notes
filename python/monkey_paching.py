# monkey patching is a technique used to dynamically update the behavior of a piece of code at run-time.
#  It is used to extend or modify the runtime code of dynamic languages such as Smalltalk, JavaScript, Objective-C, Ruby, Perl,
#  Python, Groovy, and Lisp without altering the original source code.


class Power:
    def square(self, num):
        return f"Square of {num} is: {num**2}"


obj = Power()
print(obj.square(3))


def cube(self, num):
    return f"Cube of {num} is: {num**3}"


# Monkey Patching
Power.square = cube
obj = Power()
print(obj.square(3))
