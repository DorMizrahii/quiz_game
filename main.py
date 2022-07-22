from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quizz_brain = QuizzBrain(question_bank)


while quizz_brain.still_has_question():
    quizz_brain.next_question()
quizz_brain.quizz_over()

