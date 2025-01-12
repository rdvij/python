#Lambda Functions in Python
cube = lambda x: x**3
print(cube(3))  # Output: 27

#Lambda functions can be used as an argument to other functions
square = lambda x: x**2
def squareLamma(fx, val):
    return 6 + fx(val)

print(squareLamma(square, 4))
print(squareLamma(lambda x: x**2, 4))

#Lambda functions can be used in filter() function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

#Lambda functions can also be used in list comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(type(squared_numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#Lambda functions can be used in sorting
numbers = [5, 2, 3, 1, 4]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]

#Lambda functions can be used in key argument of max() and min() functions
numbers = [5, 2, 3, 1, 4]
max_number = max(numbers, key=lambda x: x)
print(max_number)  # Output: 5

multiSort = lambda x: (x[0], x[1])
numbers = [(1, 2), (3, 1), (2, 3)]
sorted_numbers = sorted(numbers, key=multiSort)
print(sorted_numbers)  # Output: [(1, 2), (2, 3), (3, 1)]

#Lambda functions can be used in reduce() function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15