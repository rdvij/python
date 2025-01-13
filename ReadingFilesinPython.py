#Reading PDF files in Python
with open('sample.txt', 'r') as file:
    while True:
        line = file.read(128)
        if not line or len(line) == 0:
            break
        print(line + '\n')

with open('sample.txt', 'w') as file:
    file.write('Hello World!') #This will overwrite the existing content of the file

with open('sample.txt', 'r') as file:
    if file.readable():
        print(file.read().count('Hello World!'))

counter = 0
with open('sample.txt', 'a') as file:
    while counter < 5:
        file.write('Hello World!')
        counter += 1

with open('sample.txt', 'r') as file:
    if file.readable():
        print(file.read().count('Hello World!'))