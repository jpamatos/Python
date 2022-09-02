from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(q["question"], q["correct_answer"])
                 for q in question_data]

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)  # Start quiz
