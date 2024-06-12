# 1. Write a function to square each element of a list using list comprehension.
l = [1, 2, 3, 4]
print([i * i for i in l])

# 2. Create a function to filter out negative numbers from a list using list comprehension.
l = [1, 2, 3, 4, -5, -6, -7]
print([i for i in l if i < 0])
# 3. Implement a function to find the cube of each even number in a list using list comprehension.
l = [1, 2, 3, 4]
print([i * i * i for i in l if i % 2 == 0])

# 4. Write a function to extract all vowels from a given string using list comprehension.
l = ["a", "b", "c", "d", "e", "f"]
print([i for i in l if i not in ["a", "e", "i", "o", "u"]])

# 5. Create a function to convert a list of strings to uppercase using list comprehension.
l = ["a", "b", "c", "d", "e"]
print([i.upper() for i in l])

# 6. Implement a function to flatten a list of lists using list comprehension.
l = [[1, 2, 3, 4], [1, 2, 3, 4]]
print([i for k in l for i in k])

# 7. Implement a function to remove duplicates from a list using list comprehension.
l = [1, 2, 3, 4, 5, 6, 5, 7, 8, 6, 10]
print([i for i in l if l.count(i) < 2])

# 8. Create a function to reverse each string in a list using list comprehension.
l = ["python", "list", "tuple"]
print([i[::-1] for i in l])

# Given a list of tuples representing student names and their corresponding
# scores in an exam, write a Python function to create a dictionary where the keys are
# the student names and the values are their average scores
student_scores = [
    ("Alice", [85, 90, 92]),
    ("Bob", [88, 87, 85]),
    ("Charlie", [90, 92, 94]),
]
print({i: sum(n) / 2 for i, n in student_scores})

# Write a function to create a dictionary where the keys are numbers from 1 to 10, and the values are their respective squares.
print({i: i * i for i in range(1, 5)})

# Write a function that creates a dictionary from a list of tuples, where the keys are the first elements of the tuples and the values are lists of the second elements of the tuples with the same key.
student_scores = [
    ("Alice", [85, 90, 92]),
    ("Bob", [88, 87, 85]),
    ("Charlie", [90, 92, 94]),
]
print({i: n for i, n in student_scores})
