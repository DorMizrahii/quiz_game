class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.correct_answers = 0
        self.question_quantity = len(q_list)
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < self.question_quantity

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nYou got it right!")
            self.correct_answers += 1
        else:
            print("\nThat's wrong.")
        print(f"\nThe correct answer is: {correct_answer}.")
        print(f"\nYour current score is: {self.correct_answers}/{self.question_number}.\n\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)

    def quizz_over(self):
        print(f"You have completed the quizz your final score is: {self.correct_answers}/{self.question_quantity}.\n\n")
