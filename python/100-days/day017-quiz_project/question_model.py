class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"{self.text}: {self.answer}"


class QuestionBank:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.questions = []
        self.fetch_questions()

    def fetch_questions(self) -> None:
        for question in self.questions_list:
            q_text = question["question"]
            q_answer = question["correct_answer"]
            question = Question(q_text, q_answer)
            self.questions.append(question)
