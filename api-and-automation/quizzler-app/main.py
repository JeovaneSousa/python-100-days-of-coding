from question_model import Question
from trivia_api import *
from quiz_brain import QuizBrain
from ui import QuizInterface

trivia_api = TriviaApi()

question_bank = trivia_api.fetchQuestions()

quiz = QuizBrain(question_bank)

quiz_interface = QuizInterface(quiz_brain=quiz)


