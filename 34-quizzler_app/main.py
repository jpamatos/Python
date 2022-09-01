from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(q["question"], q["correct_answer"])
                 for q in question_data]

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface()

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.q_number}!")
