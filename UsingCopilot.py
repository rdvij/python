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