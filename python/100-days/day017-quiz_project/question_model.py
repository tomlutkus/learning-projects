class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"{self.text}: {self.answer}"

class QuestionBank:
    def __init__(self, questions_dict):
        self.questions_dict = questions_dict
        self.questions = []
        self.fetch_questions()

    def fetch_questions(self) -> None:
        for question in self.questions_dict:
            q_text = question["text"]
            q_answer = question["answer"]
            question = Question(q_text, q_answer)
            self.questions.append(question)
