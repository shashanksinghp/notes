class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.a <= self.max:
            self.a, self.b = self.b, self.a + self.b

            return self.a
        else:
            raise StopIteration


# create an object
numbers = PowTwo(10)

# create an iterable from the object
val = iter(numbers)

# Using next to get to the next iterator element
for i in val:
    print(i)
