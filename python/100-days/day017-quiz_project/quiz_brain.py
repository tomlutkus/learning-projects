from os import system
from random import shuffle

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = list(questions_list)
        shuffle(self.questions_list)
        self.right_answers = 0 
    
    def ask_question(self) -> bool:
        next_question = self.questions_list.pop()
        user_answer = input(
            f"{self.question_number}. {next_question.text} (True/False)\n> "
            )
        if user_answer.lower() == next_question.answer.lower():
            print("Correct!")
            return True
        else:
            print("Wrong!")
            print(f"The correct answer was: {next_question.answer}")
            return False
        
    def play_quiz(self) -> None:
        while self.question_number < 10:
            system("clear")
            self.question_number += 1
            answer_right = self.ask_question()
            if answer_right:
                self.right_answers += 1
            print(f"Your current score is: {self.right_answers}/{self.question_number}")
            input("\nPress ENTER to continue")
        
        system("clear")
        print("You've completed the quiz!")
        print(f"Final Score: {self.right_answers}/{self.question_number}")
