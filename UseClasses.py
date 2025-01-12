from KBCgame import QuestAndAnswers
import csv 

questions = []

with open("QuestionsandAnswers.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        questions.append(QuestAndAnswers(row[0], row[1:5], int(row[5])))

print(questions)