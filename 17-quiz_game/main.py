from question_model import Question
from data import question_data

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

print(question_bank[0].text, question_bank[0].answer)
