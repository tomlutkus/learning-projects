"""
Quiz Game - Answer True or False!
Author: Thomas Lutkus
"""

from question_model import Question, QuestionBank
from quiz_brain import QuizBrain
from data import question_data

def main() -> None:
    question_bank = QuestionBank(question_data)
    questions = question_bank.questions
    quiz_brain = QuizBrain(questions)
    quiz_brain.play_quiz()

if __name__ == "__main__":
    main()
