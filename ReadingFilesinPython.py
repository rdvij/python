#Reading PDF files in Python
with open('Rahul_Resume.pdf', 'rb') as file:
    while True:
        line = file.read()
        if not line or len(line) == 0:
            break
        print(line)