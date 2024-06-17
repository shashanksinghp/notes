# Write a generator function to generate Fibonacci numbers
def fibonacci(num):
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
def prime(num):
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


def nested_dictonary(nested):
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
