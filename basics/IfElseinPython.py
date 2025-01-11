# If Else in python

varString = ''' This is a multi-line string.
And this example clearly shows
how to use it.'''

if 'example' in varString:
    print(True)

# if clause with Indentation example
if 23 < len(varString):
    print(False)
    print('Printing Indentation')
else:
    print(True)
print('Not Indentation')

var = "match-case-2"

match var:
    case "match-case":
        print('Correct Match')
    case "no-match-case":
        print('Incorrect Match')
    case _:
        print('None Match')

def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(10)
check_number(30)

i = 0

while i < 20:
    print(i)
    i = i + 3
    print('In While loop')

print('Completed While loop')

while True:
    print('Check Number')
    if i == 21:
        break
    else:
        i = i + 1