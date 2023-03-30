
import requests
from question_model import *

URL = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

class TriviaApi:

    def __init__(self) -> None:
        pass
        
    def fetchQuestions(self) -> list[Question]:
        response = requests.get(url=URL, params= params)
        response.raise_for_status()
        
        data = response.json()
        result = data["results"]

        answer:bool
        question_bank = []
        
        for question in result:
            question_text = question["question"]
            question_answer = question["correct_answer"]

            if question_answer == "True":
                answer = True
            else:
                answer = False

            new_question = Question(question_text, answer)
            question_bank.append(new_question)

        return question_bank

