from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

# create a question bank from the question data.
for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))

# Initialize QuizzBank
quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("Congratulations!!! You have completed the quizz")
print(f"Your final score {quizz.score}/{quizz.question_number}")

