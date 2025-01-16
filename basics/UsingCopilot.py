# This class accepts a list of strings and returns a list of strings that are the same as the input list,
# but with the first letter of each string capitalized.
class CapitalizeStrings:
     def __init__(self, strings):
         self.strings = strings
         self.capitalized_strings = list(map(lambda x: x.capitalize(), self.strings))
         print(self.capitalized_strings)
#   
strings = input("Enter a list of strings separated by a comma: ").split(", ")
print(strings)
CapitalizeStrings(strings)
#
print("----------------------------------------------------------------")

# This function accepts a list of strings and checks if it can find it in a file.
def FindStringInFile(strings):
    with open('sample.txt', 'r') as file:
        file_content = file.read()
        for string in strings:
            if string in file_content:
                print(f"'{string}' found in the file.")
            else:
                print(f"'{string}' not found in the file.")

strings = input("Enter a list of strings separated by a comma: ").split(", ")
print(strings)
FindStringInFile(strings)
#
print("----------------------------------------------------------------")