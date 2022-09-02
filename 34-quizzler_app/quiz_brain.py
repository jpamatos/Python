import html


class QuizBrain:
    """Class to run the game"""
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        """Ask a quest to the player"""
        self.current_q = self.q_list[self.q_number]
        self.q_number += 1
        q_text = html.unescape(self.current_q.text)
        return f"Q.{self.q_number}: {q_text}"

    def still_has_questions(self):
        """Check if the game has a question to ask"""
        return self.q_number < len(self.q_list)

    def check_answer(self, user_answer):
        """Check if the user ansered correctly"""
        if user_answer.lower() == self.current_q.answer.lower():
            self.score += 1
            return True
        else:
            return False
