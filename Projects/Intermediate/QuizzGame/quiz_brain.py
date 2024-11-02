class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        q_text = self.question_list[self.question_number].text
        q_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number} : {q_text} (True or False)? : ")
        self.check_answer(answer, q_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!!")
        else:
            print("You got it wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

