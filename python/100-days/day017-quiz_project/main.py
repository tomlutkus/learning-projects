from question_model import Question, QuestionBank
from data import question_data

def main():
    for question in questions.question_list:
        print(question)






if __name__ == "__main__":
    questions = QuestionBank(question_data)
    main()