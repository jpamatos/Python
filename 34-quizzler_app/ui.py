from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Class to create quiz interface"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.true = Button(
            image=true_image,
            highlightthickness=0,
            command=self.true_pressed)
        self.true.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file="images/false.png")
        self.false = Button(
            image=false_image,
            highlightthickness=0,
            command=self.false_pressed)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Change question text"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
                f"Your final score was: {self.quiz.score}/"
                f"{self.quiz.q_number}!"
            )
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        """Send true to check the answer"""
        self.guive_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Send false to check the answer"""
        self.guive_feedback(self.quiz.check_answer("False"))

    def guive_feedback(self, is_right):
        """Check question answer and shows if user scored a point"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
