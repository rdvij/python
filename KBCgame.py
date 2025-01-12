import csv

questions = []
class QuestAndAnswers:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.question)
        for i in range(len(self.options)):
            print(str(i + 1) + ". " + self.options[i])
        print()

    def check_answer(self, answer):
        if answer < 1 or answer > 4:
            return "InvalidOption"
        return self.correct_option == answer

with open("QuestionsandAnswers.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        questions.append(QuestAndAnswers(row[0], row[1:5], int(row[5])))

score = 0

startOfGameMessage = """
Welcome to the KBC game. \nYou will be asked 5 questions, each with 4 options, and you have to choose the correct option.
\nFor each correct answer, you will get 1 point, and for each wrong answer, you will lose 1 point.
\nMake sure to enter the option number (1, 2, 3, or 4) as your answer.
\nMinimum score required to win: 3
\n
***** Let's start the game! *****
"""

print(startOfGameMessage)

i = 0
while i < 5:
    questions[i].display_question()
    answer = int(input("Enter your answer: "))

    if questions[i].check_answer(answer) == "InvalidOption":
        print("Invalid answer! Please enter a number between 1 and 4.")
        print("Your current score is: " + str(score))

    elif questions[i].check_answer(answer):
        print("Correct answer!")
        score += 1
        print("Your current score is: " + str(score))
        i += 1

    else:
        print("Wrong answer!")
        score -= 1
        print("Your current score is: " + str(score))
        i += 1

print("----------------------------------------------------------------")
print(
    "\n\nThank you for playing the game!"
    + "\nYour final score is: "
    + str(score)
    + "\nYou lose! :-("
    if score < 3
    else "\nYou win! :-) "
)
print("----------------------------------------------------------------")