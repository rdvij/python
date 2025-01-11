import time
import os

print(os.system('python3 --version'))

# Check and print Morning/Afternoon/Evening/Night
currHour = time.strftime('%H')

if (4 < int(currHour) < 12):
    print('Morning Greeting!')
elif (12 < int(currHour) < 4):
    print('Afternoon Greeting!')
elif (4 < int(currHour) < 8):
    print('Evening Greeting!')
else :
    print('Night Greeting!')


def multiNumbers(*numbers):
    result = 1
    for number in numbers:
        result = result * number
        print(result)
    return result

multiNumbers(1, 2, 3, 4, 5)

def usingDict(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['city'])
    kwargs.update({'city': 'Texas'})
    print(kwargs)
    return kwargs

print(usingDict(name='John', age=30, city='New York'))
