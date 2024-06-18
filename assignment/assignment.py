from dataclasses import dataclass

# Write a generator function to generate Fibonacci numbers
def fibonacci(num: int):
    a, b = 0, 1
    while num > a:
        yield a
        a, b = b, a + b


for fib in fibonacci(10):
    print(fib)


# list comprehension to find the transpose of a matrix
matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print([[matrix[j][i] for j in range(0, len(matrix))] for i in range(0, len(matrix[0]))])

# Create a generator that yields prime numbers
def prime(num: int):
    for j in range(2, num):
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            yield j


for i in prime(50):
    print(i)

# flatten a nested dictionary into a single dictionary.
nested_dict = {
    "one": {"a": 5, "b": {"c": 6, "d": {"e": 7}}},
    "two": 7,
    "three": {"a": 5, "b": 6, "c": 7},
}
flatten_dict = {}
nested_key = []


def nested_dictonary(nested: int) -> dict:
    for k, v in nested.items():
        if isinstance(v, dict):
            nested_key.append(k)
            nested_dictonary(v)
        else:
            nested_key.append(k)
            if nested_key:
                flatten_dict[".".join(nested_key)] = v
                nested_key.pop()
            else:
                flatten_dict[k] = v
    nested_key.clear()
    return flatten_dict


print(nested_dictonary(nested_dict))

# Design a class representing a computer with components such as CPU, RAM,
# and Hard Drive. Use composition to model the relationship between the
# computer and its components.


@dataclass
class Ram:
    capacity: str
    stick_type: str
    clock_frequency: str


@dataclass
class Cpu:
    type: str
    generation: str
    core: int
    frequency: str


@dataclass
class Storage:
    type: str
    size: str


class Computer:
    _instance = None

    def __new__(cls, ram, cpu, storage):
        if cls._instance is None:
            cls._instance = super(Computer, cls).__new__(cls)
        return cls._instance

    def __init__(self, ram, cpu, storage):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def update_ram(self, updated_ram: object):
        self.ram = updated_ram
        return self.ram

    def update_cpu(self, updated_cpu: object):
        self.cpu = updated_cpu
        return self.cpu

    def update_storage(self, updated_storage: object):
        self.storage = updated_storage
        return self.storage


r = Ram("8GB", "DDR4", "2400MHz")
c = Cpu("i5", "8Gen", 6, "2.80MHz")
s = Storage("SSD", "500GB")
computer = Computer(r, c, s)
c2 = Computer(r, c, s)
print(computer)
print(c2)
