class QuizBrain:
    def __init__(self,q_bank):
        self.question_number = 0
        self.question_bank = q_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.question} (True/false)?: ")
        self.question_number += 1
        self.check_answer(current_question.correct_answer,answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_bank):
           return True
        else:
            False


    def check_answer(self,correct_answer,user_answer):
        if correct_answer.lower() == user_answer.lower():
            print(f"You got it right!")
            self.score += 1
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is : {self.score}/{self.question_number}\n\n")
        else:
            print("That's wrong!")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is : {self.score}/{self.question_number}\n\n")

# quiz = QuizBrain()
# quiz.next_question