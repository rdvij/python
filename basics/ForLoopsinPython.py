varString = ''' This is a multi-line string.
And this example clearly shows
how to use it.'''

print(len(varString))

print(varString[0:5])

name = 'Rajan'
print(name[-4:-2])

if '22' in varString:
    doForloop()

# For loop function
def doForloop():
    for char in varString:
        print(char)

print(varString.upper())

#Iterate over a list using while loop
listOfNumbers = [1, 2, 3, 4, 5]
