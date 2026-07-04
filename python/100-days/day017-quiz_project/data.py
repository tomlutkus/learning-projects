import requests
import html

url = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url)

if response.status_code == 200:
    url_data = response.json()

    question_data = url_data["results"]

    for question in question_data:
        clean_question = html.unescape(question["question"])
        question["question"] = clean_question

else:
    """
    This is a fallback questionnaire, for the case the request fails
    """
    question_data = [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Politics",
            "question": "Denmark has a monarch.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Entertainment: Video Games",
            "question": "In Monster Hunter Generations, guild style is a type of hunting style.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "History",
            "question": "The Fourth Crusade lasted from 1095-1099 AD.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Until 1939, Laos was called Siam.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Entertainment: Music",
            "question": "Michael Jackson wrote The Simpsons song &quot;Do the Bartman&quot;.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Animals",
            "question": "The Platypus is a mammal.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "History",
            "question": "United States President John F. Kennedy was assassinated during his presidential motorcade in Atlanta, Georgia on November 22nd, 1963.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "hard",
            "category": "Science: Mathematics",
            "question": "L&#039;H&ocirc;pital was the mathematician who created the homonymous rule that uses derivatives to evaluate limits with indeterminations.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Entertainment: Television",
            "question": "&quot;The Simpsons&quot; family is named after creator Matt Groening&#039;s real family.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Mathematics",
            "question": "An isosceles triangle has two sides of equal length as opposed to three.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
    ]

    for question in question_data:
        clean_question = html.unescape(question["question"])
        question["question"] = clean_question
