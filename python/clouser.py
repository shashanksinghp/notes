# Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.
def greet(name):
    # inner function
    def display_name():
        print("Hi", name)

    # call inner function
    display_name()


# call outer function
greet("John")
