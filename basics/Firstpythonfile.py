print("Simplest python Code")

''' Working with variables and data types'''

x = 10
y = '10'
z = x + int(y)
b = str(x) + y
str = "Hello World"

print(str[3])

complexNum = 1 + 2j
print(complexNum)

# Data type of a variable
print(type(x))
print(type(y))
print(type(z))
print(type(b))
print((type(complexNum)) == complex)

# List and Tuples
varList = [1, 2, 3, 4, 5]
varList.append(6)
print(varList)
varTuple = (1, 2, 3, 4, 5)
varTuple = varTuple + (6,)
print(varTuple)

print(type(varList))
print(type(varTuple))

# Dictionary, a collection of key-value pairs
varDict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print(varDict)
varDict.update({'age': 31})
print(varDict)
varDict.clear()
varDict = {
    'country': 'USA'
}
print(varDict)
print(type(varDict))

# Taking input from user
userInput = input("Enter your name: ")
print("Hello, " + userInput)

# Multiple line String
varString = ''' This is a multi-line string.
And this example clearly shows
how to use it.'''
print(varString)