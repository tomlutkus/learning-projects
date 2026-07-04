class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"{self.text}: {self.answer}"

class QuestionBank:
    def __init__(self, question_data):
        self.question_list = []
        self.fetch_questions(question_data)

    def fetch_questions(self, question_data) -> None:
        for question in question_data:
            q_text = question["text"]
            q_answer = question["answer"]
            question = Question(q_text, q_answer)
            self.question_list.append(question)
